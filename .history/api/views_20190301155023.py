# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers


class Quote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.TodoSerializer