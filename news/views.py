from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

from django.core.mail import send_mail

import os

from .models import News
from .forms import EmailNewsForm


# class NewsListView(ListView):
#     """
#     Alternative news list view
#     """

#     # queryset = News.published.all()
#     model = News
#     context_object_name = 'newss'
#     paginate_by = 3
#     template_name = 'news.html'


def news(request):
    news_list = News.objects.all().order_by('-date')

    # pagination 3 news per page
    paginator = Paginator(news_list, 1)
    page_number = request.GET.get('page', 1)

    try:
        newss = paginator.page(page_number)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        newss = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'newss': newss})

# def news_detail(request, news_id: int):
def news_detail(request, year, month, day, news_id):
    # news = get_object_or_404(News, pk=news_id)
    # news = get_object_or_404(News, pk=news_id, slug=news_id, date__year=year, date__month=month, date__day=day)
    news = get_object_or_404(News, date__year=year, date__month=month, date__day=day, slug=news_id)

    return render(request, 'news_detail.html', {'news': news})


def news_share(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    sent = False

    # Form submitted
    if request.method == 'POST':
        form = EmailNewsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ... send email
            news_url = request.build_absolute_uri(news.get_absolute_url())
            subject = f'{cd['name']} recommends yo read {news.headline}'
            message = f'News: {news.headline} at {news_url}'

            send_mail(subject, message, os.getenv('EMAIL_HOST_USER'), [cd['to']])

            sent = True

            print(f'{news_url=} - {subject=} - {message=}')
    else:
        form = EmailNewsForm()
    return render(request, 'news_share.html', {'form': form, 'news':news})




