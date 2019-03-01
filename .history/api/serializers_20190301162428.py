# api/serializers.py
from rest
from quotes import models


class QuoteSerializer(serializers):
    class Meta:
        fields = (
            'id',
            'quote',
            'author',
        )
        model = models.Quote