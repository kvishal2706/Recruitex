# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Skills, Gender_type, SubscribedUsers


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'phone', 'is_staff','profile_photo',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone','profile_photo','Major_skill','address','about_me','skills_tag','skills','interests','facebook_link','twitter_link','instagram_link','youtube_link','applied_jobs')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('phone','profile_photo','Major_skill','address','about_me','skills_tag','skills','interests','facebook_link','twitter_link','instagram_link','youtube_link','applied_jobs',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Skills)
admin.site.register(Gender_type)
admin.site.register(SubscribedUsers,SubscribedUsersAdmin)