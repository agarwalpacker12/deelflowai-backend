from django.db import models
import uuid

# 1. Core Business Metrics
class BusinessMetrics(models.Model):
    total_revenue = models.DecimalField(max_digits=18, decimal_places=2)
    active_users = models.IntegerField()
    properties_listed = models.IntegerField()
    ai_conversations = models.DecimalField(max_digits=18, decimal_places=2)
    total_deals = models.IntegerField()
    monthly_profit = models.DecimalField(max_digits=18, decimal_places=2)
    voice_calls_count = models.IntegerField()
    report_date = models.DateField()

    def __str__(self):
        return f"Metrics on {self.report_date}"


# 2. Historical Data
class HistoricalMetrics(models.Model):
    metric_type = models.CharField(max_length=50)   # e.g. revenue, active_users
    metric_value = models.DecimalField(max_digits=18, decimal_places=2)
    record_date = models.DateField()

    def __str__(self):
        return f"{self.metric_type} - {self.record_date}"


# 3. Real-Time Activity
class ActivityFeed(models.Model):
    user_id = models.IntegerField()
    action_type = models.CharField(max_length=100)  # e.g. deal_completed, login
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} by {self.user_id} at {self.timestamp}"


# 4. Compliance & System Health
class ComplianceStatus(models.Model):
    compliance_percent = models.DecimalField(max_digits=5, decimal_places=2)
    audit_trail = models.TextField()
    system_health = models.CharField(max_length=50)  # e.g. healthy, warning
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Compliance {self.compliance_percent}% ({self.system_health})"
    
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    subscription_status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50, default="user")
    level = models.IntegerField(default=1)
    points = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationship
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="users"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"