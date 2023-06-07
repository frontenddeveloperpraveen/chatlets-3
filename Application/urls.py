from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('home',views.Home,name="Home"),
    path('chat',views.Chat,name="chat"),
    path('admin/', admin.site.urls),
    path('check-room',views.Check_room,name="check-room"),
    path('<str:room>/',views.Room_join,name="check-room"),
    path('send',views.Send,name="Send"),
    path('getMessages/<str:room>/',views.message,name="Message"),
    path('download',views.Download,name="download"),
    path("",views.Page,name="Page"),
    path("lobbyuser",views.Lobby,name="Lobby"),
    path("removeroom",views.Remove_room,name="Remove_room"),
    path("user-connection-dead",views.User_inactive,name="User_inactive"),
    path("checkuser",views.checkuser,name="checkuser"),
    path('/playground',views.Playground, name='Playground'),
    path('chat-bot-send',views.Chat_bot, name='Playground'),
]
