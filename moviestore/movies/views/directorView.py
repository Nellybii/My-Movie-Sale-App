from rest_framework import generics
from ..serializers import DirectorSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Director

class DirectorList(generics.ListAPIView):
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Director.objects.all()

class DirectorCreate(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
    
class DirectorUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
