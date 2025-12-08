from django.contrib import admin
from .models import SubscriptionType, UserSubscription

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_days']

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription_type', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active', 'end_date']
