from django.db import models

from django.urls import reverse



class News(models.Model):
    headline = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, unique_for_date='date')
    # slug = models.SlugField(max_length=250, null=True, unique_for_date='date')
    body = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.headline

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id, self.date.year, self.date.month, self.date.day, self.slug])






