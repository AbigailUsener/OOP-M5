from django.db import models


class Movie(models.Model):
    name = models.TextField()
    release_year = models.IntegerField()
    main_genre = models.TextField()

def add_movie(name,release_date,genres):
    movie = Movies(name=name,release_year=release_date,main_genre=genres)
    movie.save()
    return movie

def view_All():
    movie = Movies.objects.all()
    return movie

def view_by_movie_name(movie_name):
    try:
        movie = Movies.objects.get(name=movie_name)
        return movie
    except:
        return None

def update_release_year(movie_name, new_year):
    movie = Movies.objects.get(name=movie_name)
    movie.release_year = new_year
    movie.save()
    return movie

def delete_movie(movie_name):
    movie = Movies.objects.get(name=movie_name)
    movie.delete()
    return movie