from rest_framework import viewsets

from cards.models import Card
from cards.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    """ViewSet for cards."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer

