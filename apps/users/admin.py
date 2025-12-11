from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TrainerCertificate
class CertificateInline(admin.TabularInline):
    model = TrainerCertificate
    extra = 1
    fields = ('title', 'issued_by', 'date_issued')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'is_manager', 'is_staff']
    list_filter = ['is_manager', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Додаткова інформація (Тренер/Клієнт)', {
            'fields': ('phone_number', 'is_manager', 'bio')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'is_manager', 'bio')
        }),
    )

    inlines = [CertificateInline]