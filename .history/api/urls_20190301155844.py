# demo_project/urls.py
from django.contrib import admin
from django.urls import include, path

from . import view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', views.Quote.as_view()),
]