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
    source_link = models.CharField(max_length=255, default="")
    skills_used = models.ManyToManyField("Skills")
    project_description=models.TextField(default="")
    project_images = models.ImageField(upload_to=f"accounts/projects/{title}/", default="")

class Award(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    gender = models.ForeignKey('Gender_type', on_delete=models.CASCADE, default="", null=True, blank=True)
    phone=models.CharField(max_length=12,null = False, blank = False, default="")
    profile_photo = models.ImageField(upload_to="accounts/profile_photos", default="default_profile.png" , null=True, blank=True)
    Major_skill = models.CharField(max_length=30,help_text="Eg: Frontend Developer and designer",  null=True, blank=True, default="")
    address = models.CharField(max_length=50, default="", help_text="Hyderabad, India", null=True, blank=True)
    about_me = models.TextField( null=True, blank=True, default="")
    skills_tag = models.ManyToManyField("Skills")
    skills = models.CharField(max_length=255,  null=True, blank=True, default="")
    interests = models.CharField(max_length=255,  null=True, blank=True, default="")
    facebook_link = models.CharField(default="", max_length=255, null=True, blank=True)
    twitter_link = models.CharField(default="", max_length=255, null=True, blank=True)
    instagram_link = models.CharField(default="", max_length=255, null=True, blank=True)
    youtube_link = models.CharField(default="", max_length=255, null=True, blank=True)
    projects=models.ManyToManyField('Project',default=None, blank=True)
    applied_jobs = models.ManyToManyField("Jobs.Jobs",blank=True)
    awards = models.ForeignKey("Award",on_delete=models.CASCADE, blank=True, null=True)
    slug=models.SlugField(default="",blank=True,null=True,db_index=True)
    is_recruiter = models.BooleanField(default=False)
    


class SubscribedUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    created_date = models.DateTimeField('Date created', default=timezone.now)
    
    def __str__(self):
        return self.email

    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    feedback = models.TextField()
    created_date = models.DateTimeField('Date created', default=timezone.now)
    
    def __str__(self):
        return f"{self.name}, {self.email}"
