from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/create', views.create_review, name='create_review'),
    path('review/<int:review_id>', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete', views.delete_review, name='delete_review'),
]




