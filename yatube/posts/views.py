
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse('Главная страница')
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    return HttpResponse(f'Пост {slug}')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
