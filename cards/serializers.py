from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    """Serializer for cards."""
    class Meta:
        """Default meta."""
        model = Card
        fields = '__all__'
