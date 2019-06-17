from django.shortcuts import render
from blog.models import Movie
from blog.models import Weather
from blog.models import JD_goods
import MySQLdb
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.paginator import Paginator

# Create your views here.
def login(request):
    return render(request,'index.html')

def show_movie(request):  
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print('page param ：',page)

    movies=Movie.objects.all()
    paginator=Paginator(movies,25)
    page_num=paginator.num_pages
    print('page param ：',page_num)
    page_movies=paginator.page(page)
    if page_movies.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_movies.has_previous():
        previous_page=page-1
    else:    
        previous_page=page

    return render(request,'Mymovie.html',
                {
                    'movies':page_movies,
                    'page_num':range(1,page_num+1),
                    'curr_page':page,
                    'next_page':next_page,
                    'previous_page':previous_page
                }
            )

def search_weather(request):   
   q = request.GET.get('q','')
   weathers_list = Weather.objects.filter(city=q)
   return render(request,'Weather.html',
        {
               'weathers_list':weathers_list
               
        })

def show_weather(request):     
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print('page param ：',page)

    weathers = Weather.objects.all()
    paginator=Paginator(weathers,25)
    page_num=paginator.num_pages
    print('page param ：',page_num)
    page_weathers=paginator.page(page)
    if page_weathers.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_weathers.has_previous():
        previous_page=page-1
    else:    
        previous_page=page
    
    return render(request,'base.html',
        {
                'weathers':page_weathers,
                'page_num':range(1,page_num+1),
                'curr_page':page,
                'next_page':next_page,
                'previous_page':previous_page
        }
    )

def show_goods(request):
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print('page param ：',page)

    goods = JD_goods.objects.all()
    paginator=Paginator(goods,25)
    page_num=paginator.num_pages
    print('page param ：',page_num)
    page_goods=paginator.page(page)
    if page_goods.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_goods.has_previous():
        previous_page=page-1
    else:    
        previous_page=page



    return render(request,'Jdgoods.html',
      {
            'goods':page_goods,
            'page_num':range(1,page_num+1),
            'curr_page':page,
            'next_page':next_page,
            'previous_page':previous_page
           
      }
    )
