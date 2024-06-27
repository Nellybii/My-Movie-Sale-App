from rest_framework import generics
from ..serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Review

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
    
class ReviewUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
