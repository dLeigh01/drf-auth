from rest_framework import serializers
from .models import GameReview

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('reviewer', 'game', 'system', 'rating', 'review')
        model = GameReview