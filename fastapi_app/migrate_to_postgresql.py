"""
Database migration script from SQLite to PostgreSQL
This script migrates data from the existing SQLite database to PostgreSQL
"""

import os
import sys
import django
from django.conf import settings
from django.db import connections
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deelflowAI.settings')
django.setup()

logger = logging.getLogger(__name__)

class DatabaseMigrator:
    """Database migration class"""
    
    def __init__(self, sqlite_path: str, postgres_url: str):
        self.sqlite_path = sqlite_path
        self.postgres_url = postgres_url
        self.sqlite_conn = None
        self.postgres_conn = None
    
    def connect_databases(self):
        """Connect to both databases"""
        try:
            # Connect to SQLite
            self.sqlite_conn = connections['default']
            
            # Connect to PostgreSQL
            self.postgres_conn = psycopg2.connect(self.postgres_url)
            self.postgres_conn.autocommit = True
            
            logger.info("Connected to both databases successfully")
        except Exception as e:
            logger.error(f"Failed to connect to databases: {e}")
            raise
    
    def migrate_tables(self):
        """Migrate all tables from SQLite to PostgreSQL"""
        try:
            # Get all table names from SQLite
            with self.sqlite_conn.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
                tables = [row[0] for row in cursor.fetchall()]
            
            logger.info(f"Found {len(tables)} tables to migrate")
            
            for table in tables:
                self.migrate_table(table)
            
            logger.info("Migration completed successfully")
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            raise
    
    def migrate_table(self, table_name: str):
        """Migrate a specific table"""
        try:
            logger.info(f"Migrating table: {table_name}")
            
            # Get table structure from SQLite
            with self.sqlite_conn.cursor() as cursor:
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = cursor.fetchall()
                
                # Get all data from SQLite
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
            
            if not rows:
                logger.info(f"Table {table_name} is empty, skipping")
                return
            
            # Create table in PostgreSQL if it doesn't exist
            self.create_postgres_table(table_name, columns)
            
            # Insert data into PostgreSQL
            self.insert_data_to_postgres(table_name, columns, rows)
            
            logger.info(f"Successfully migrated {len(rows)} rows from {table_name}")
        except Exception as e:
            logger.error(f"Failed to migrate table {table_name}: {e}")
            raise
    
    def create_postgres_table(self, table_name: str, columns: list):
        """Create table in PostgreSQL"""
        try:
            with self.postgres_conn.cursor() as cursor:
                # Check if table exists
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = %s
                    )
                """, (table_name,))
                
                if cursor.fetchone()[0]:
                    logger.info(f"Table {table_name} already exists in PostgreSQL")
                    return
                
                # Create table
                column_definitions = []
                for col in columns:
                    col_name = col[1]
                    col_type = self.convert_sqlite_type(col[2])
                    col_not_null = "NOT NULL" if col[3] else ""
                    col_primary_key = "PRIMARY KEY" if col[5] else ""
                    
                    column_def = f"{col_name} {col_type} {col_not_null} {col_primary_key}".strip()
                    column_definitions.append(column_def)
                
                create_sql = f"CREATE TABLE {table_name} ({', '.join(column_definitions)})"
                cursor.execute(create_sql)
                
                logger.info(f"Created table {table_name} in PostgreSQL")
        except Exception as e:
            logger.error(f"Failed to create table {table_name}: {e}")
            raise
    
    def convert_sqlite_type(self, sqlite_type: str) -> str:
        """Convert SQLite data type to PostgreSQL data type"""
        type_mapping = {
            'INTEGER': 'INTEGER',
            'TEXT': 'TEXT',
            'REAL': 'REAL',
            'BLOB': 'BYTEA',
            'NUMERIC': 'NUMERIC',
            'VARCHAR': 'VARCHAR',
            'CHAR': 'CHAR',
            'DATETIME': 'TIMESTAMP',
            'DATE': 'DATE',
            'TIME': 'TIME',
            'BOOLEAN': 'BOOLEAN'
        }
        
        # Handle common SQLite types
        if 'INT' in sqlite_type.upper():
            return 'INTEGER'
        elif 'TEXT' in sqlite_type.upper() or 'VARCHAR' in sqlite_type.upper():
            return 'TEXT'
        elif 'REAL' in sqlite_type.upper() or 'FLOAT' in sqlite_type.upper():
            return 'REAL'
        elif 'BLOB' in sqlite_type.upper():
            return 'BYTEA'
        elif 'NUMERIC' in sqlite_type.upper() or 'DECIMAL' in sqlite_type.upper():
            return 'NUMERIC'
        elif 'DATETIME' in sqlite_type.upper() or 'TIMESTAMP' in sqlite_type.upper():
            return 'TIMESTAMP'
        elif 'DATE' in sqlite_type.upper():
            return 'DATE'
        elif 'TIME' in sqlite_type.upper():
            return 'TIME'
        elif 'BOOLEAN' in sqlite_type.upper():
            return 'BOOLEAN'
        else:
            return 'TEXT'  # Default fallback
    
    def insert_data_to_postgres(self, table_name: str, columns: list, rows: list):
        """Insert data into PostgreSQL table"""
        try:
            with self.postgres_conn.cursor() as cursor:
                # Prepare column names
                column_names = [col[1] for col in columns]
                placeholders = ', '.join(['%s'] * len(column_names))
                
                # Insert data
                insert_sql = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
                cursor.executemany(insert_sql, rows)
                
                logger.info(f"Inserted {len(rows)} rows into {table_name}")
        except Exception as e:
            logger.error(f"Failed to insert data into {table_name}: {e}")
            raise
    
    def close_connections(self):
        """Close database connections"""
        if self.sqlite_conn:
            self.sqlite_conn.close()
        if self.postgres_conn:
            self.postgres_conn.close()
        logger.info("Closed database connections")

def main():
    """Main migration function"""
    # Configuration
    sqlite_path = "db.sqlite3"  # Path to existing SQLite database
    postgres_url = "postgresql://user:password@localhost/deelflowai"  # PostgreSQL connection URL
    
    # Create migrator instance
    migrator = DatabaseMigrator(sqlite_path, postgres_url)
    
    try:
        # Connect to databases
        migrator.connect_databases()
        
        # Migrate tables
        migrator.migrate_tables()
        
        logger.info("Migration completed successfully!")
        
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        sys.exit(1)
    
    finally:
        # Close connections
        migrator.close_connections()

if __name__ == "__main__":
    main()
