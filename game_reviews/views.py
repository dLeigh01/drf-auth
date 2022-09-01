from rest_framework import generics
from .models import GameReview
from .permissions import IsOwnerOrReadOnly
from .serializers import GameSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = GameReview.objects.all()
    serializer_class = GameSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = GameReview.objects.all()
    serializer_class = GameSerializer