from django.shortcuts import render

# Create your views here.
# snippets/views.py
from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

import random


class RandomQuote(generics.ListAPIView):
    
    queryset = Quote.objects.all().filter(id = pick_random_object())
    serializer_class = QuoteSerializer
    




