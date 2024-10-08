from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics

from chat.models import Chat
from chat.serializers import ChatSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    model = Chat
    serializer_class = ChatSerializer

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(mentor=user) | Q(students=user))