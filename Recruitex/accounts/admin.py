# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Skills, Gender_type, SubscribedUsers,Feedback, Project
from .models import Qualification,WorkandExperience,Blog


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    prepopulated_fields = {"slug":("username",)}
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'phone', 'is_staff','profile_photo',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone','dob','age','gender','profile_photo','major_skill','salary','address','about_me','languages','skills_tag','interests','facebook_link','twitter_link','instagram_link','youtube_link','projects','applied_jobs','cv','resume','qualifications','work_experience','slug','is_recruiter',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('phone','dob','age','gender','profile_photo','major_skill','salary','address','languages','about_me','skills_tag','interests','facebook_link','twitter_link','instagram_link','youtube_link','projects','applied_jobs','cv','resume','qualifications','work_experience','slug','is_recruiter',)}),)


admin.site.register(Skills)
admin.site.register(Gender_type)
admin.site.register(Project)
admin.site.register(Qualification)
admin.site.register(WorkandExperience)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(SubscribedUsers,SubscribedUsersAdmin)
admin.site.register(Blog)