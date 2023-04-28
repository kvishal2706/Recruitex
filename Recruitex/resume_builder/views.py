from django.shortcuts import render,HttpResponse
import requests
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser,WorkandExperience,Project

def build(request):
    pass

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

    # response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)
    return HttpResponse(f'Hello {about_me}')