from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    # path('', views.NewsListView.as_view(), name='news'),
    # path('<int:news_id>', views.news_detail, name='news_detail'),
    # path('<int:news_id>/<int:year>/<int:month>/<int:day>/<slug:news>', views.news_detail, name='news_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:news_id>', views.news_detail, name='news_detail'),
    path('<int:news_id>/share/', views.news_share, name='news_share')
]
