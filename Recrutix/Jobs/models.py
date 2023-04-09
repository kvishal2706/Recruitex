from datetime import date
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse


class Tag(models.Model):
    name=models.CharField(max_length=200, unique=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Jobs_type(models.Model):
    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Job_Duration(models.Model):
    name = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    title=models.CharField(max_length=250,null=False,blank=False, default="")
    designation=models.CharField(max_length=250,null=True,blank=True)
    location=models.CharField(help_text="Enter company's location (city name)",max_length=255,null=True,blank=True)
    salary=models.CharField(max_length=50,null=True,blank=True)
    type=models.ForeignKey('Jobs_type',default=None ,on_delete=models.CASCADE)
    #qualification
    #preffered qualification
    logo = models.ImageField(upload_to="Jobs/job_logo",default="default_job.png", null=True,blank=True)
    # tag=models.ManyToManyField('Tag',blank=True)
    job_Category=models.ForeignKey('Tag',default=None ,on_delete=models.CASCADE,null=True, blank=True)
    job_duration_type=models.ForeignKey('Job_Duration',default=None ,on_delete=models.CASCADE,null=True, blank=True)
    about_job=models.TextField(null=True,blank=True)
    about_company=models.TextField(null=True,blank=True)
    workings=models.TextField(null=True,blank=True)
    skills_required = models.ManyToManyField("accounts.Skills", default="", blank=True)
    no_of_openings = models.IntegerField(default=10, null=True,blank=True)
    embedded_location_url = models.TextField(help_text="Embeded url from maps of company only src",blank=True, null=False)
    date = models.DateField(auto_now_add=True)
    recruiter=models.ForeignKey("accounts.CustomUser",related_name='recruiter_name',null=True, blank=True,on_delete=models.CASCADE)
    slug=models.SlugField(default="",blank=True,null=False,db_index=True,unique=True)
    job_applied_users = models.ManyToManyField("accounts.CustomUser", related_name='job_applied_users', blank=True)

    def save(self,*args, **kwargs):
        Slug = str(self.title) + "-" + str(self.designation)
        self.slug = slugify(Slug)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
    def get_absolute_url(self):
        return reverse("job_details", args=[self.slug])
    
    
class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False,blank=False)
    about_you = models.TextField(null=True,blank=True)
    why_you = models.TextField(name=False,blank=False)
    job = models.ForeignKey("Jobs", on_delete=models.DO_NOTHING, default="")
    def __str__(self):
        return f"{self.first_name}, {self.email}"
