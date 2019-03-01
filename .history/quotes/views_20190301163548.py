from django.shortcuts import render

# Create your views here.
# snippets/views.py
from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

import random

class QuoteView(generics.RetrieveAPIView):
    queryset = Quote.objects.all().filter(id = pick_random_object())
    serializer_class = QuoteSerializer

def get_queryset():
    return 
def pick_random_object():
    return random.randrange(1, Quote.objects.all().count() + 1)

