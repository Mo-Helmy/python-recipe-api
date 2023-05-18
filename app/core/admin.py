"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


# class UserAdmin(admin.ModelAdmin):
#     ordering = ['id']
#     list_display = ('email', 'name', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal Info'), {'fields': ('name',)}),
#         (
#             _('Permissions'),
#             {
#                 'fields': (
#                     'is_active',
#                     'is_staff',
#                     'is_superuser',
#                 )
#             }
#         ),
#         (_('Important dates'), {'fields': ('last_login',)}),
#     )
#     readonly_fields = ['last_login']
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email',
#                 'password1',
#                 'password2',
#                 'name',
#                 'is_active',
#                 'is_staff',
#                 'is_superuser',
#             ),
#         }),
#     )


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    list_display = ('email', 'name', 'is_superuser', )
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)
