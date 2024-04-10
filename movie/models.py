from typing import Any
from django.db import models
from django.contrib.auth.models import User

# from django.contrib import auth


class Classification(models.Model):
    class ClassificationEnum(models.TextChoices):
        CLASS_A = 'A', 'Classification A'
        CLASS_B = 'B', 'Classification B'
        CLASS_C = 'C', 'Classification C'

    name = models.CharField(
        verbose_name="Classification name",
        choices=ClassificationEnum.choices,
        max_length=2, 
    )

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True, null=True)
    create_uid_classification = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='create_uid_classification')
    write_uid_classification = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='write_uid_classification')

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20, help_text="Genre of the movie")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True, null=True)
    create_uid_genre = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='create_uid_genre')
    write_uid_genre = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='write_uid_genre')

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True, null=True)
    create_uid_director = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='create_uid_director')
    write_uid_director = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='write_uid_director')

    def __str__(self) -> str:
        return self.name
    

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Movies.Status.PUBLISHED)


class Movies(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    date = models.DateField(verbose_name='Fecha de Estreno')
    url = models.URLField(blank=True)

    # Genre should be Many2many
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    clasificacion = models.ForeignKey(Classification, null=True, on_delete=models.SET_NULL)  # ForeignKey to create Many2one

    directors = models.ManyToManyField(Director)  # ManyToManyField to Many2many. through: to create a specific join table with extra info

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)
    create_uid_movies = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='create_uid_movies')
    write_uid_movies = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='write_uid_movies')

    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

    class Meta:
        ordering  = ['-create_date']
        indexes = [
            models.Index(fields=['-create_date'])
        ]

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # Many2one
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)  # Many2one
    watch_again = models.BooleanField()

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True, null=True)
    create_uid_review = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='create_uid_review')
    write_uid_review = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='write_uid_review')

    def __str__(self) -> str:
        return self.text
    









