from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    date = models.DateField()
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        # return f'{self.id}, {self.title}'
        return self.title







