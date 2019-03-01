from django.shortcuts import render

# Create your views here.
# snippets/views.py
from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class Quoteview(generics.RetrieveAPIView):
    queryset = Quote.objects.all()[0]
    serializer_class = QuoteSerializer

