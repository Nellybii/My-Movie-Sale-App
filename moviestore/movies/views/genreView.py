from rest_framework import generics
from ..serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Genre

class GenreList(generics.ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Genre.objects.all()

class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
    
class GenreUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class =GenreSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
