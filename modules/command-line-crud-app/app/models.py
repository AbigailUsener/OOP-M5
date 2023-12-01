from django.db import models


class Movie(models.Model):
    name = models.TextField()
    release_year = models.IntegerField()
    main_genre = models.TextField()

def add_movie(name,release_date,genres):
    movie = Movie(name=name,release_year=release_date,main_genre=genres)
    movie.save()
    return movie

def view_All():
    movie = Movie.objects.all()
    return movie

def view_name(movie_name):
    try:
        movie = Movie.objects.get(name=movie_name)
        return movie
    except:
        return None

def update(movie_name, new_year):
    movie = Movie.objects.get(name=movie_name)
    movie.release_year = new_year
    movie.save()
    return movie

def delete(movie_name):
    movie = Movie.objects.get(name=movie_name)
    movie.delete()