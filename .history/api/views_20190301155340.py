# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers


class Quote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quote.objects.
    serializer_class = serializers.ModelSerializer

    def pick_random_object():
   return random.randrange(1, MyModel.objects.all().count() + 1)

    def get_queryset(self):
      return models.Quote.objects.all().filter(id = pick_random_object())