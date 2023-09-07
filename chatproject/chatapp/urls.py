from django.urls import path
from .import views

urlpatterns=[
    path('',views.users,name="users_list"),
    path('chatroom/<str:receiver>/',views.chatroom,name="chat_room"),
    path('unread_msg/',views.unread_message,name='unread_msg')
]
