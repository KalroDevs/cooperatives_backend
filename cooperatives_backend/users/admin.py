from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Customize the admin interface for CustomUser
class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the list view
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    
    # Fields to search
    search_fields = ('username', 'email')
    
    # Fields to filter by
    list_filter = ('is_staff', 'is_active', 'role', 'county', 'position')
    
    # Define fieldsets to show in the detailed view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role')}),
        ('Important dates', {'fields': ('last_login',)}),
        ('More', {'fields': ('position','county',)}),
    )
    
    # Fields to show during user creation in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'county', 'position', 'is_staff', 'is_active')}
        ),
    )
    
    # Fields used for ordering in the admin view
    ordering = ('username',)

# Register the CustomUser model and CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(County)
class CountiesAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SubCounty)
class SubCountiesAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Ward)
class WardsAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



