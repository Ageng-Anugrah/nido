from django.contrib import admin
from app_profile.models import (
    UserProfile
)
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'photo',
        'phone_number',
        'secondary_email',
        'line_id',
        'birth_date',
        'birth_place',
        'home_address',
        'current_address',
    )


admin.site.register(UserProfile, UserProfileAdmin)
