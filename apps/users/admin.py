from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # стовпці списку
    list_display = ['username', 'email', 'phone_number', 'is_manager', 'is_staff']
    
    # фільтри 
    list_filter = ['is_manager', 'is_staff', 'is_superuser', 'is_active']
    
    # поля редагування юзера
    # беремо секції UserAdmin.fieldsets, додаємо свою
    fieldsets = UserAdmin.fieldsets + (
        ('Додаткова інформація', {'fields': ('phone_number', 'is_manager')}),
    )
    
    # поля створення нового юзера
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'email', 'is_manager')}),
    )
