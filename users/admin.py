from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'city', 'state']
    list_filter = ['user_type', 'state']
    search_fields = ['user__username', 'user__email', 'city', 'state']
