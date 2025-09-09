from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BusinessMetrics
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .decorators import unauthenticated_user,allowed_users,admin_only

from django.shortcuts import render
import io
from json.encoder import JSONEncoder
from logging import NullHandler
import locale
import re
import requests
import time
from typing import IO
from django.http import response
from django.views.decorators.csrf import ensure_csrf_cookie
import os
from datetime import datetime
from django.db import Error
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http import HttpResponse
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http.response import JsonResponse
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.http import HttpResponse
from html import escape
import datetime

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from django.utils.decorators import decorator_from_middleware
from corsheaders.middleware import CorsMiddleware

import json
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.auth.hashers import check_password


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    email = request.data.get("username")
    password = request.data.get("password")

    print("Attempting login for:", email)
    print("Attempting login for:", password)
    # Check if user exists
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(
            {"status": "error", "message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Verify password
    if not check_password(password, user.password):
        return Response(
            {"status": "error", "message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Generate JWT token
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Custom response format
    data = {
        "status": "success",
        "message": "User logged in successfully",
        "data": {
            "token": access_token,
            "user": {
                "id": user.id,
                "uuid": str(user.uuid),
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role
            }
        }
    }
    return Response(data, status=status.HTTP_200_OK)


# @csrf_exempt
# def loginpage(request):
#     if request.method == 'POST':
#         # Handle both JSON and form-data requests
#         if request.content_type == 'application/json':
#             try:
#                 data = json.loads(request.body.decode("utf-8"))
#                 username = data.get('username')
#                 password = data.get('password')
#             except Exception:
#                 return JsonResponse({"status": "Error", "result": {"response": "Invalid JSON format"}}, status=400)
#         else:
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#         print("Authenticated user:", user)

#         if user is not None:
#             login(request, user)  # ✅ Django session created
#             return JsonResponse({"status": "Success", "result": {"response": "Login successful"}})
#         else:
#             return JsonResponse({"status": "Error", "result": {"response": "Username or Password is incorrect"}}, status=401)

#     return JsonResponse({"status": "Error", "result": {"response": "Only POST method allowed"}}, status=405)


# @csrf_exempt
# #@unauthenticated_user
# def loginpage(request):
#     if request.method == 'POST':
#         Username = request.POST.get('username')
#         Password = request.POST.get('password')

#         # Normal Django authentication
#         user = authenticate(request, username=Username, password=Password)
#         if user is not None:
#             login(request, user)
#             return redirect('user')
#             # If you want JsonResponse instead of redirect, keep below lines
#             # res = {"status": "Success", "result": {"responce": "login successful"}}
#             # return JsonResponse(res)
#         else:
#             res = {"status": "Error", "result": {"responce": "Username Or Password is Incorrect"}}
#             return JsonResponse(res)

#     return render(request, 'FDA/login.html')


# API view to get the latest total revenue
@api_view(['GET'])
def get_total_revenue(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'total_revenue': str(latest_metrics.total_revenue)})
	return Response({'total_revenue': None})

# API view to get the latest active users
@api_view(['GET'])
def get_active_users(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'active_users': latest_metrics.active_users})
	return Response({'active_users': None})

# API view to get the latest properties listed
@api_view(['GET'])
def get_properties_listed(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'properties_listed': latest_metrics.properties_listed})
	return Response({'properties_listed': None})

# API view to get the latest AI conversations
@api_view(['GET'])
def get_ai_conversations(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'ai_conversations': str(latest_metrics.ai_conversations)})
	return Response({'ai_conversations': None})

# API view to get the latest total deals
@api_view(['GET'])
def get_total_deals(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'total_deals': latest_metrics.total_deals})
	return Response({'total_deals': None})

# API view to get the latest monthly profit
@api_view(['GET'])
def get_monthly_profit(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'monthly_profit': str(latest_metrics.monthly_profit)})
	return Response({'monthly_profit': None})

# API view to get the latest voice calls count
@api_view(['GET'])
def get_voice_calls_count(request):
	latest_metrics = BusinessMetrics.objects.order_by('-report_date').first()
	if latest_metrics:
		return Response({'voice_calls_count': latest_metrics.voice_calls_count})
	return Response({'voice_calls_count': None})

# API view to get the latest compliance status
@api_view(['GET'])
def get_compliance_status(request):
	from .models import ComplianceStatus
	latest_status = ComplianceStatus.objects.order_by('-updated_at').first()
	if latest_status:
		return Response({
			'compliance_percent': str(latest_status.compliance_percent),
			'audit_trail': latest_status.audit_trail,
			'system_health': latest_status.system_health,
			'updated_at': latest_status.updated_at
		})
	return Response({'compliance_percent': None, 'audit_trail': None, 'system_health': None, 'updated_at': None})

# API view to get the latest audit trail data
@api_view(['GET'])
def get_audit_trail_data(request):
	from .models import ComplianceStatus
	latest_status = ComplianceStatus.objects.order_by('-updated_at').first()
	if latest_status:
		return Response({'audit_trail': latest_status.audit_trail})
	return Response({'audit_trail': None})

# API view to get the latest system health metrics
@api_view(['GET'])
def get_system_health_metrics(request):
	from .models import ComplianceStatus
	latest_status = ComplianceStatus.objects.order_by('-updated_at').first()
	if latest_status:
		return Response({'system_health': latest_status.system_health})
	return Response({'system_health': None})

# API view to get revenue & user growth chart data
@api_view(['GET'])
def get_revenue_user_growth_chart_data(request):
	from .models import HistoricalMetrics
	revenue_data = HistoricalMetrics.objects.filter(metric_type='revenue').order_by('date')
	user_data = HistoricalMetrics.objects.filter(metric_type='active_users').order_by('date')
	revenue_chart = [{'date': r.date, 'value': r.value} for r in revenue_data]
	user_chart = [{'date': u.date, 'value': u.value} for u in user_data]
	return Response({
		'revenue_chart': revenue_chart,
		'user_growth_chart': user_chart
	})

# API view to get monthly trend data
@api_view(['GET'])
def get_monthly_trend_data(request):
	from .models import HistoricalMetrics
	# Assuming 'monthly_trend' is a metric_type in HistoricalMetrics
	trend_data = HistoricalMetrics.objects.filter(metric_type='monthly_trend').order_by('date')
	trend_chart = [{'date': t.date, 'value': t.value} for t in trend_data]
	return Response({'monthly_trend_chart': trend_chart})

# API view to get historical performance data
@api_view(['GET'])
def get_historical_performance(request):
	from .models import HistoricalMetrics
	performance_data = HistoricalMetrics.objects.all().order_by('date')
	performance_chart = [
		{
			'date': p.date,
			'metric_type': p.metric_type,
			'value': p.value
		} for p in performance_data
	]
	return Response({'historical_performance': performance_chart})

# API view to get live activity feed
@api_view(['GET'])
def get_live_activity_feed(request):
	from .models import ActivityFeed
	activities = ActivityFeed.objects.order_by('-timestamp')[:50]  # latest 50 activities
	feed = [
		{
			'user': a.user,
			'action_type': a.action_type,
			'description': a.description,
			'timestamp': a.timestamp
		} for a in activities
	]
	return Response({'live_activity_feed': feed})

# API view to get user actions and timestamps
@api_view(['GET'])
def get_user_actions_timestamps(request):
	from .models import ActivityFeed
	activities = ActivityFeed.objects.order_by('-timestamp')[:50]
	actions = [
		{
			'user': a.user,
			'action_type': a.action_type,
			'timestamp': a.timestamp
		} for a in activities
	]
	return Response({'user_actions_timestamps': actions})

# API view to get deal completions and scheduling
@api_view(['GET'])
def get_deal_completions_scheduling(request):
	from .models import ActivityFeed
	completions = ActivityFeed.objects.filter(action_type='deal_completed').order_by('-timestamp')[:50]
	scheduling = ActivityFeed.objects.filter(action_type='deal_scheduled').order_by('-timestamp')[:50]
	completions_data = [
		{
			'user': c.user,
			'description': c.description,
			'timestamp': c.timestamp
		} for c in completions
	]
	scheduling_data = [
		{
			'user': s.user,
			'description': s.description,
			'timestamp': s.timestamp
		} for s in scheduling
	]
	return Response({
		'deal_completions': completions_data,
		'deal_scheduling': scheduling_data
	})
