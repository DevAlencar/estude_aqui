from django.urls import path

from chat import views

urlpatterns = [
    path("chat/", views.ChatListCreateView.as_view(), name="chat_list_create"),
]