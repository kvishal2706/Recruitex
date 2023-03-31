# from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class Skills(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Gender_type(models.Model):
    name = models.CharField(max_length=7)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    source_link = models.CharField(max_length=255)
    skills_used = models.ManyToManyField("Skills")
    project_description=models.TextField(default="")
    project_images = models.ImageField(upload_to=f"accounts/projects/{title}/", default="")


class CustomUser(AbstractUser):
    gender = models.ForeignKey('Gender_type', on_delete=models.CASCADE, default="", null=True)
    phone=models.CharField(max_length=12,null = False, blank = False, default="")
    profile_photo = models.ImageField(upload_to="accounts/profile_photos", default="default_profile.png" ,blank=True)
    applied_jobs = models.ManyToManyField("Jobs.Jobs")
    Major_skill = models.CharField(max_length=30,help_text="Eg: Frontend Developer and designer", null=False, blank=False, default="")
    address = models.CharField(max_length=50, default="", help_text="Hyderabad, India")
    about_me = models.TextField(blank=False, null=False, default="")
    skills_tag = models.ManyToManyField("Skills")
    skills = models.CharField(max_length=255, blank=False, null=False, default="")
    interests = models.CharField(max_length=255, blank=False, null=False, default="")
    facebook_link = models.CharField(default="", max_length=255)
    twitter_link = models.CharField(default="", max_length=255)
    instagram_link = models.CharField(default="", max_length=255)
    youtube_link = models.CharField(default="", max_length=255)
    projects=models.ManyToManyField('Project',default=None)
    


class SubscribedUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    created_date = models.DateTimeField('Date created', default=timezone.now)
    
    def __str__(self):
        return self.email

    
