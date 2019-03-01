# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers


class Quote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models..objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer