# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers


class Quote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quote.objects.
    serializer_class = serializers.ModelSerializer

    def get_queryset(self):
      return odel.objects.all().filter(id = pick_random_object())