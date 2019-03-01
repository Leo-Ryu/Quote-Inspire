# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers

import random


class Quote(generics.RetrieveAPIView):

    queryset = models.Quote.objects.all().filter(id = pick_random_object())   
    serializer_class = serializers.ModelSerializer

    def get_queryset():
        return 
    def pick_random_object():
        return random.randrange(1, models.Quote.objects.all().count() + 1)

    