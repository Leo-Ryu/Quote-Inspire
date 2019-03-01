from django.db import models
from django.db.models.aggregates import Count


# Create your models here.from random import randint

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.quote

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
