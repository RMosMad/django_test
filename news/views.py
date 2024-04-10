from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News


def news(request):
    news_list = News.objects.all().order_by('-date')

    # pagination 3 news per page
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        newss = paginator.page(page_number)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        newss = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'newss': newss})


def news_detail(request, news_id: int, year, month, day):
    # news = get_object_or_404(News, pk=news_id)
    news = get_object_or_404(News, pk=news_id, slug=news_id, date__year=year, date__month=month, date__day=day)

    return render(request, 'news_detail.html', {'news': news})




