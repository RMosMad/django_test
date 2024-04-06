from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    date = models.DateField()
    clasificacion = models.CharField(max_length=10)
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        # return f'{self.id}, {self.title}'
        return self.title
    

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Many2one
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)  # Many2one
    watch_again = models.BooleanField()

    def __str__(self) -> str:
        return self.text







