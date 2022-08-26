from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from chat.models import Room, chatMessage
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request, 'index.html')

def send(request,room):
    # return HttpResponse("Reached")
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    new_message=chatMessage.objects.create(message=message,username=username,room_id=room_id)
    new_message.save()
    return HttpResponse("Message Recieved")


def room(request, room):
    roomDetails=Room.objects.get(name=room)
    username=request.GET.get('username')
    return render(request,'room.html',{
        'room':room,
        'username':username,
        'roomDetails':roomDetails
    })

def checkRoom(request):
    room = request.POST['roomname']
    userName = request.POST['username']
    roomPassword=request.POST['password']
    if Room.objects.filter(name=room).exists():
          if Room.objects.filter(name=room).values_list('password',flat=True).first()==roomPassword:
            return redirect('/'+room+'?username='+userName)
          else:
            return render(request,'index.html')
    else:
            new_room = Room.objects.create(name=room,password=roomPassword)
            new_room.save()
            return redirect('/'+room+'?username='+userName)
        

def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=chatMessage.objects.filter(room_id=room_details.id)
    return JsonResponse({
        "messages":list(messages.values())
    })