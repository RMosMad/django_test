from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User



class News(models.Model):
    headline = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=False, unique_for_date='date')
    body = models.TextField()
    date = models.DateField()

    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)
    create_uid = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='create_uid_news')
    write_uid_movies = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='write_uid_news')

    def __str__(self) -> str:
        return self.headline

    def get_absolute_url(self):
        # return reverse('news:news_detail', args=[self.pk])
        # return reverse('news:news_detail', args=[self.pk, self.date.year, self.date.month, self.date.day, self.slug])
        return reverse('news:news_detail', args=[self.date.year, self.date.month, self.date.day, self.slug])






