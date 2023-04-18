from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

@login_required
def check_room(request, slug):
    user1=request.user
    user2=CustomUser.objects.get(slug=slug)
    try:
        room = Room.objects.get(users__in=[user1, user2]).distinct() 
    except:
        room=None
    if room:
        return redirect('room',id=room.id)
    
    else:
        room= Room()
        room.save()
        room.users.add(user1,user2)
        return redirect('room',id=room.id)


# Create your views here.
@login_required
def room(request, id):
    print(f'{id}')
    room_mod=Room.objects.get(id=id)
    print('22222')
    return render(request, 'chat/room.html', {'room': room_mod})

# def checkview(request):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})