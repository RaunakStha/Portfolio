from django.shortcuts import render
from .models import Room
from .form import RoomForm
# Create your views here.


# rooms = [
#     {'id':1, 'name':'lets learn python!'},
#     {'id':2, 'name':'design with me'},
#     {'id':3, 'name':'Frontend developer'},


# ]



def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'baseapp/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'baseapp/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)

    context ={'form':form}
    return render(request, 'baseapp/room_form.html',context)