# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers

import random


class Quote(generics.RetrieveAPIView):

    queryset = get_queryset()        
    serializer_class = serializers.ModelSerializer

    def pick_random_object(self):
        return random.randrange(1, models.Quote.objects.all().count() + 1)

    def get_queryset(self):
        return models.Quote.objects.all().filter(id = self.pick_random_object())