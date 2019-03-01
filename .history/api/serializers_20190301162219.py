# api/serializers.py
from rest_framework import serializers
from quotes import models


class QuoteSerializer(serializers.):
    class Meta:
        fields = (
            'id',
            'quote',
            'author',
        )
        model = models.Quote