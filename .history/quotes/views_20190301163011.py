from django.shortcuts import render

# Create your views here.
# snippets/views.py
from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer