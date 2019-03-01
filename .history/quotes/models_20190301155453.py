from django.db import models
from django.db.models.aggregates import Count

from random import randint

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.quote
