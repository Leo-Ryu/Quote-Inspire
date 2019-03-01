# api/views.py
from rest_framework import generics

from quotes import models
from . import serializers

import random


class Quote(generics.RetrieveAPIView):

    queryset = models.Quote.objects.all().filter(id = random.randrange(1, models.Quote.objects.all().count() + 1)   
    serializer_class = serializers.ModelSerializer

    