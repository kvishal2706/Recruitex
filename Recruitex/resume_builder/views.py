from django.shortcuts import render,HttpResponse
import requests
from accounts.models import CustomUser,WorkandExperience,Project
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

# def build(request):

#     # url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"
#     try: 
#         user=CustomUser.objects.get(username=request.user.username)
#     except:
#         user=None
    
#     if user:
#         about_me=user.about_me
#         project_count=user.projects.all()
#         all_projects={}
#         i=0#         for project in project_count:
#             all_projects[i]=project.project_description

#     # payload = {
#     #     "about_me": about_me,
#     #     "result_type": "single"
#     # }
#     # headers = {
#     #     "content-type": "application/json",
#     #     "X-RapidAPI-Key": "23e5c6f754msh29baab6aeed4d3ap19db48jsncaa861d6bff6",
#     #     "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
#     # }

#     # response = requests.request("POST", url, json=payload, headers=headers)

#     # print(response.text)
#     return HttpResponse(f'Hello {about_me}')



api_key= os.getenv("OPENAI_KEY",None)

def chatbot(request):
    chatbot_response= None
    try: 
        user=CustomUser.objects.get(username=request.user.username)
    except:
        user=None
    
    if api_key is not None:
        openai.api_key = api_key
        about_me=user.about_me
        qualifications=user.qualification
        prompt_about_me = f"paraphrase this and make it more appropriate for my resume:  {about_me}"
        prompt_qualification = f"paraphrase this qualifications and make it more appropriate for my resume:  {qualifications}"
        response_about_me= openai.Completion.create(
            engine= 'text-davinci-003',
            prompt=prompt_about_me,
            max_tokens=256,
            # stop="."
            # hello world. how are you?
            temperature=0.5
        )
        chatbot_response_about_me= response_about_me["choices"][0]["text"]

        print(chatbot_response_about_me)

        response_qualification= openai.Completion.create(
            engine= 'text-davinci-003',
            prompt=prompt_qualification,
            max_tokens=256,
            # stop="."
            # hello world. how are you?
            temperature=0.5
        )
        chatbot_response_qualification= response_qualification["choices"][0]["text"]
        print(chatbot_response_qualification)
    return HttpResponse(f"About me: {chatbot_response_about_me} Qualifications :{chatbot_response_qualification}")
    # return render(request,'main.html',{'response':chatbot_response})