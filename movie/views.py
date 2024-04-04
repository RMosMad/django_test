from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from .models import Movies



def home(request):
    # return HttpResponse('<h1>Home Page</h1>')
    search_term = request.GET.get('inputSearchMovie')
    if search_term:
        movies = Movies.objects.filter(title__icontains=search_term)
    else:
        movies = Movies.objects.all()
    return render(request, 'home.html', {'search_term': search_term, 'movies': movies})

def about(request):
    return HttpResponse('<h1>About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def detail(request, movie_id: int):
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})







