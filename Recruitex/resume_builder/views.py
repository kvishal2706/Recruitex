from django.shortcuts import render,HttpResponse
import requests
from accounts.models import CustomUser,WorkandExperience,Project

def build(request):

    # url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"
    try: 
        user=CustomUser.objects.get(username=request.user.username)
    except:
        user=None
    
    if user:
        about_me=user.about_me
        project_count=user.projects.all()
        all_projects={}
        i=0
        for project in project_count:
            all_projects[i]=project.project_description

    # payload = {
    #     "about_me": about_me,
    #     "result_type": "single"
    # }
    # headers = {
    #     "content-type": "application/json",
    #     "X-RapidAPI-Key": "23e5c6f754msh29baab6aeed4d3ap19db48jsncaa861d6bff6",
    #     "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
    # }

    # response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)
    return HttpResponse(f'Hello {about_me}')