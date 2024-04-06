from django.test import TestCase

from movie.models import Movies

from datetime import datetime


class MovieTestCase(TestCase):

    def test_movie(self):

        movie = Movies(title='Título Prueba', description='Descripción Prueba', clasificacion='C')

        self.assertEqual(movie.title, 'Título Prueba')
        self.assertEqual(movie.description, 'Descripción Prueba')
        self.assertEqual(movie.clasificacion, 'C')

