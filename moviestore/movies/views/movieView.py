from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from ..serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Movie
from django.conf import settings

class MovieList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        modified_movies = [] 
        
        def get_cleaned_url(image_url):
            base_url = settings.BASE_URL
            if image_url.startswith(base_url):
                return image_url[len(base_url):]
            return image_url

        for movie in queryset:
            image_url = get_cleaned_url(movie.image.url)
            movie.image = image_url
            modified_movies.append(movie)

        queryset = Movie.objects.all()
        for movie in queryset:
          return queryset 



class MovieCreate(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class =MovieSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
