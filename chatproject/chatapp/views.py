from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Message
from django.http import JsonResponse
# Create your views here.

def users(request):
    users=User.objects.exclude(username=request.user)
    return render(request,'users.html',{"users":users})

def chatroom(request,receiver):
    users=User.objects.exclude(username=request.user)

    receiver=User.objects.get(id=receiver)
    sender=request.user
    message=Message.objects.filter(sender=sender,receiver=receiver)|Message.objects.filter(sender=receiver,receiver=sender).order_by('timestamp')
    unread_msg=Message.objects.filter(receiver=request.user,is_read=False)
    for unread in unread_msg:
        unread.is_read=True
        unread.save()
    return render(request,'chatroom.html',{"message": message,"sender": sender,"receiver": receiver,'users':users})

def unread_message(request):
    receiver=request.user.id
    unread_msg=Message.objects.filter(receiver=receiver,is_read=False)
    unread_msglist=[
        {
            'sender':unread.sender.username,
            'receiver':unread.receiver.username,
            'message':unread.message,
            'is_read':unread_msg.count(),
        }
        for unread in unread_msg
    ]
    return JsonResponse(unread_msglist,safe=False)
