from django.test import TestCase
from app import models
# Create your tests here.
class TestMovie(TestCase):
    def Test_add_movie(self):
        movies=models.add_movie(
            "Hunger Games",
            "2012",
            "Fiction"
        )
        self.assertContains(movies)
        
    def test_view_all(self):
        movies=models.add_movie(
            "Hunger Games",
            "2012",
            "Fiction"
        )
        test = models.view_All()
        self.assertEqual(len(test),1)

    def test_update(self):
        movies=models.add_movie(
            "Hunger Games",
            "2012",
            "Fiction"
        )
        thing=models.update('Hunger Games','2010')
        self.assertEqual(thing,movies)

    def test_search_name(self):
        movies=models.add_movie(
            "Hunger Games",
            "2012",
            "Fiction"
        )
        thing=models.view_name("Hunger Games")
        self.assertEqual(thing.name,movies.name)

    def test_delete(self):
        movies=models.add_movie(
            "Hunger Games",
            "2012",
            "Fiction"
        )
        models.delete('Hunger Games')
        self.assertEqual(len(models.view_All()),0)