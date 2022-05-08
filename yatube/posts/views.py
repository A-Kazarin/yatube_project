
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse('Главная страница')
    template = 'posts/index.html'
    context = {
        # В словарь можно передать переменную
        'title': text,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница'}
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Пост {slug}')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
