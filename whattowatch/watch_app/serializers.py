from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'rotten_tomatos', 'hulu_url',
        'amazon_url', 'hbo_max_url', 'netflix_url', 'movie_id')

class AddMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','rotten_tomatos',)
