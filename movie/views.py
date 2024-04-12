from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect

from .models import Movies, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required



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
    reviews = Review.objects.filter(movie=movie)
    
    return render(request, 'detail.html', {'movie': movie, 'reviews': reviews})

@login_required
def create_review(request, movie_id: int):
    movie = get_object_or_404(Movies, pk=movie_id)
    if request.method == 'GET':
        context = {
            'form': ReviewForm, 
            'movie': movie
        }
        return render(request, 'create_review.html', context)
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('movie:detail', new_review.movie.pk)
        except ValueError:
            return render(request, 'create_review.html', {'form': ReviewForm, 'error': 'Wrong data passed in'})

@login_required     
def edit_review(request, review_id: int):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie:edit_review.html', {'form':form, 'review': review})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('movie:detail', review.movie.pk)
        except ValueError:
            return render(request, 'edit_review.html', {'form':form, 'review': review, 'error':'Bad data in form'})

@login_required
def delete_review(request, review_id: int):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('movie:detail', review.movie.pk)







