# api/serializers.py
from rest_framework import serializers
from quotes import models


class Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'quote',
            'author',
        )
        model = models.Quote