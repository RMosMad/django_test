from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register_account, name='register'),
    path('logout/', views.logout_account, name='logout'),
    path('login/', views.login_account, name='login'),
]
