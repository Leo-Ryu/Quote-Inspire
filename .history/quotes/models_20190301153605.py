from django.db import models

# Create your models here.
class Quote(models.model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.quote.
