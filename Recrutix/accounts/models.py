from datetime import date
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
    
class Qualification(models.Model):
    institute_name = models.CharField(max_length=255, blank=False, null=False)
    degree_type = models.CharField(max_length=255, blank=False, null=False)
    field_of_study = models.CharField(max_length=255, blank=False, null=False)
    start_year = models.IntegerField(blank=False, null=False)
    end_year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return F"{self.institute_name}, {self.degree_type}"

class WorkandExperience(models.Model):
    job_title = models.CharField(max_length=255, blank=False, null=False)
    company_name = models.CharField(max_length=255, blank=False, null=False)
    joining_date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    leaving_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    experience_description = models.TextField(blank=False, name=False)
    
    
    def __str__(self):
        return f"{self.job_title}, {self.company_name}"

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    phone=models.CharField(max_length=12,null = False, blank = False, default="")
    gender = models.ForeignKey('Gender_type', on_delete=models.CASCADE, default="", null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="accounts/profile_photos", default="default_profile.png" , null=True, blank=True)
    salary = models.CharField(max_length=50, default="", blank=True, null=True)
    address = models.CharField(max_length=50, default="", help_text="Hyderabad, India", null=True, blank=True)
    about_me = models.TextField( null=True, blank=True, default="")
    languages = models.CharField(max_length=100, blank=True, null=True, default="")
    interests = models.CharField(max_length=255,  null=True, blank=True, default="")
    facebook_link = models.CharField(default="", max_length=255, null=True, blank=True)
    twitter_link = models.CharField(default="", max_length=255, null=True, blank=True)
    instagram_link = models.CharField(default="", max_length=255, null=True, blank=True)
    youtube_link = models.CharField(default="", max_length=255, null=True, blank=True)
    major_skill = models.CharField(max_length=30,help_text="Eg: Frontend Developer and designer",  null=True, blank=True, default="")
    skills_tag = models.ManyToManyField("Skills")
    projects=models.ManyToManyField('Project',default=None, blank=True)
    applied_jobs = models.ManyToManyField("Jobs.Jobs",blank=True)
    cv = models.FileField(upload_to=f"accounts/cv", max_length=255, default="", null=True, blank=True)
    resume = models.FileField(upload_to="accounts/resume", max_length=255, default="", null=True, blank=True)
    qualifications = models.ManyToManyField('Qualification', blank=True)
    work_experience = models.ManyToManyField('WorkandExperience', blank=True)
    awards = models.ManyToManyField("Award", blank=True)
    slug=models.SlugField(default="",blank=True,null=False,db_index=True)
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
