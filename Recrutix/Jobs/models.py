from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    Jobs_types=(
        ('Online','Work-From-Home'),
        ('Offline','From Office')
    )

    title=models.CharField(max_length=50,null=False,blank=False)
    designation=models.CharField(max_length=50,null=False,blank=False)
    location=models.CharField(max_length=70,null=False,blank=False)
    salary=models.CharField(max_length=20,null=False,blank=False)
    type=models.CharField(max_length=20,choices=Jobs_types,blank=False,null=False)
    # qualification
    #preffered qualification
    tag=models.ManyToManyField('Tag',blank=True)
    about_job=models.TextField(null=False,blank=False)
    about_company=models.TextField(null=False,blank=False)
    workings=models.TextField(null=False,blank=False)
    date=models.DateTimeField(auto_now_add=True)
    recruiter=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    slug=models.SlugField(default="",blank=True,null=False,db_index=True)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("job_details", args=[self.slug])
    

