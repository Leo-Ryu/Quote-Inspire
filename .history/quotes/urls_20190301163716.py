# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quotes import views

urlpatterns = [
    path('quote/<int:pk>', views.QuoteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)