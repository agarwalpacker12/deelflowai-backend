from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from .views import ChangePasswordView

urlpatterns = [

    path("create-user/", views.create_user, name="create-user"),
    
    path('login/', views.login_user, name='login'),

    path('api/total-revenue/', views.get_total_revenue, name='total-revenue'),

    path('api/active-users/', views.get_active_users, name='active-users'),

    path('api/properties-listed/', views.get_properties_listed, name='properties-listed'),

    path('api/ai-conversations/', views.get_ai_conversations, name='ai-conversations'),

    path('api/total-deals/', views.get_total_deals, name='total-deals'),

    path('api/monthly-profit/', views.get_monthly_profit, name='monthly-profit'),

    path('api/voice-calls-count/', views.get_voice_calls_count, name='voice-calls-count'),

    path('api/compliance-status/', views.get_compliance_status, name='compliance-status'),

    path('api/audit-trail-data/', views.get_audit_trail_data, name='audit-trail-data'),

    path('api/system-health-metrics/', views.get_system_health_metrics, name='system-health-metrics'),

    path('api/revenue-user-growth-chart-data/', views.get_revenue_user_growth_chart_data, name='revenue-user-growth-chart-data'),

    path('api/monthly-trend-data/', views.get_monthly_trend_data, name='monthly-trend-data'),

    path('api/historical-performance/', views.get_historical_performance, name='historical-performance'),

    path('api/live-activity-feed/', views.get_live_activity_feed, name='live-activity-feed'),

    path('api/user-actions-timestamps/', views.get_user_actions_timestamps, name='user-actions-timestamps'),

    path('api/deal-completions-scheduling/', views.get_deal_completions_scheduling, name='deal-completions-scheduling'),

]