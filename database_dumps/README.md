# 🗄️ DeelFlowAI Database Dumps

**Generated**: October 9, 2025  
**Database Type**: SQLite  
**Total Records**: 19  
**Dump Timestamp**: 20251009_155447

---

## 📁 Files Overview

### 1. **SQL Dump** - `deelflowai_dump_20251009_155447.sql`
- **Purpose**: Complete database backup with schema and data
- **Format**: SQL statements (CREATE TABLE, INSERT INTO)
- **Size**: ~50KB
- **Usage**: Restore entire database or migrate to another system

### 2. **JSON Dump** - `deelflowai_dump_20251009_155447.json`
- **Purpose**: Structured data export for analysis and integration
- **Format**: JSON with metadata and table data
- **Size**: ~15KB
- **Usage**: Data analysis, API integration, or application import

### 3. **CSV Dumps** - `csv_dumps_20251009_155447/`
- **Purpose**: Individual table exports for spreadsheet analysis
- **Format**: CSV files (one per table)
- **Files**: 5 CSV files
- **Usage**: Excel analysis, data visualization, or selective imports

### 4. **Summary Report** - `dump_summary_20251009_155447.md`
- **Purpose**: Human-readable overview and usage instructions
- **Format**: Markdown documentation
- **Usage**: Reference guide for using the dumps

---

## 📊 Data Summary

| Table | Records | Description |
|-------|---------|-------------|
| **Properties** | 5 | Real estate listings across different cities |
| **Leads** | 3 | Potential buyers/sellers with contact info |
| **Deals** | 3 | Property transactions in various stages |
| **AI Analyses** | 3 | AI-generated property insights |
| **Deal Milestones** | 5 | Transaction progress tracking |

---

## 🚀 Usage Instructions

### **Restore from SQL Dump**
```bash
# Create new database and restore
sqlite3 new_database.db < deelflowai_dump_20251009_155447.sql

# Verify restoration
sqlite3 new_database.db ".tables"
```

### **Import JSON Data**
```python
import json

# Load JSON dump
with open('deelflowai_dump_20251009_155447.json', 'r') as f:
    data = json.load(f)

# Access table data
properties = data['tables']['properties']['data']
leads = data['tables']['leads']['data']

# Process data as needed
for property in properties:
    print(f"Property: {property['address']} - ${property['price']}")
```

### **Import CSV Files**
```python
import pandas as pd

# Load individual CSV files
properties_df = pd.read_csv('csv_dumps_20251009_155447/properties.csv')
leads_df = pd.read_csv('csv_dumps_20251009_155447/leads.csv')

# Analyze data
print(properties_df.describe())
print(leads_df.groupby('status').size())
```

### **PostgreSQL Migration**
```bash
# Convert SQLite dump to PostgreSQL
# 1. Install pgloader or use manual conversion
# 2. Modify data types as needed
# 3. Import into PostgreSQL

psql -U username -d database_name -f converted_dump.sql
```

---

## 🏗️ Database Schema

### **Core Tables**
- **Properties**: Real estate listings with full details
- **Leads**: Potential buyers/sellers with contact information
- **Deals**: Property transactions with pricing and status
- **AI Analyses**: AI-generated insights and confidence scores
- **Deal Milestones**: Transaction progress tracking

### **Supporting Tables**
- **Users**: System users and authentication
- **Organizations**: Multi-tenant organization data
- **Roles & Permissions**: Access control system
- **Campaigns**: Marketing campaign management
- **Business Metrics**: Performance and analytics data

---

## 🔧 Technical Details

### **Data Types Handled**
- ✅ **Decimals**: Converted to floats in JSON/CSV
- ✅ **Datetimes**: ISO format strings
- ✅ **Foreign Keys**: Referenced by ID
- ✅ **JSON Fields**: Preserved as JSON strings
- ✅ **Boolean Values**: True/False

### **Character Encoding**
- **Format**: UTF-8
- **Special Characters**: Properly escaped
- **Unicode**: Full support

### **File Formats**
- **SQL**: Standard SQLite syntax
- **JSON**: Pretty-printed with 2-space indentation
- **CSV**: Comma-separated with headers

---

## 📋 Sample Data

### **Properties Sample**
```csv
id,address,city,state,zipcode,property_type,price,bedrooms,bathrooms
1,123 Main Street,New York,NY,10001,apartment,750000.0,3,2.0
2,456 Oak Avenue,Los Angeles,CA,90210,house,1200000.0,4,3.0
3,789 Pine Street,Chicago,IL,60601,condo,450000.0,2,2.0
```

### **Leads Sample**
```csv
id,name,email,phone,address,city,state,status,source
1,John Smith,john@email.com,555-0123,123 Main St,New York,NY,new,website
2,Jane Doe,jane@email.com,555-0456,456 Oak Ave,Los Angeles,CA,qualified,referral
```

---

## ⚠️ Important Notes

### **Data Privacy**
- Contains sample/test data only
- No real personal information
- Safe for development and testing

### **Compatibility**
- **SQLite**: Direct import
- **PostgreSQL**: Requires data type conversion
- **MySQL**: Requires syntax adjustments
- **MongoDB**: Requires JSON transformation

### **Limitations**
- Static snapshot at dump time
- No real-time updates
- Foreign key relationships preserved as IDs

---

## 🎯 Use Cases

### **Development**
- Set up local development environment
- Test with realistic data
- Debug application logic

### **Testing**
- Load test data into staging
- Verify data integrity
- Test migration scripts

### **Analysis**
- Analyze property market data
- Study lead conversion patterns
- Review deal performance

### **Backup & Recovery**
- Complete database backup
- Point-in-time recovery
- Disaster recovery planning

---

## 📞 Support

For questions about these database dumps:
- **Documentation**: See `dump_summary_20251009_155447.md`
- **Schema**: Refer to Django models in `deelflow/models.py`
- **API**: Check `API_DOCUMENTATION.md` for endpoint details

---

**Generated by**: DeelFlowAI Database Dump Tool v1.0.0  
**Last Updated**: October 9, 2025  
**Status**: ✅ Ready for Use
