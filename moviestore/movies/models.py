from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(upload_to='genres')

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField()
    picture = models.ImageField(upload_to='directors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration = models.IntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.id}"
