from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Genre, Director, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if 'username' not in validated_data:
            raise serializers.ValidationError({"username": "This field is required."})
        if 'email' not in validated_data:
            raise serializers.ValidationError({"email": "This field is required."})
        if 'password' not in validated_data:
            raise serializers.ValidationError({"password": "This field is required."})
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'biography']

from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'price', 'release_date', 'genre', 'director', 'duration', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'movie', 'review_text', 'rating', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
