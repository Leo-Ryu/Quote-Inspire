# snippets/serializers
from rest_framework import serializers
from .models import Quote, LANGUAGE_CHOICES, STYLE_CHOICES


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('id', 'quote', 'text')