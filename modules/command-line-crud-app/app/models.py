from django.db import models


class Games(models.Model):
    name = models.TextField()
    release_year = models.IntegerField()
    main_genre = models.TextField()
    developer = models.TextField()
    main_character = models.TextField()

def add_game(name,release_date,genres,dev,main_character):
    game = Games(name=name,release_year=release_date,main_genre=genres,developer=dev,main_character=main_character)
    game.save()
    return game

def view_All():
    game = Games.objects.all()
    return game

def view_by_publisher(dev):
    game = Games.objects.filter(developer=dev)
    return game

def view_by_game_name(game_name):
    try:
        game = Games.objects.get(name=game_name)
        return game
    except:
        return None

def update_publisher(game_name, new_publisher):
    game = Games.objects.get(name=game_name)
    game.developer = new_publisher
    game.save()
    return game

def delete_game(game_name):
    game = Games.objects.get(name=game_name)
    game.delete()
    return game