
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    #return HttpResponse('Главная страница')
    template = 'posts/index.html'
    #context = {
        # В словарь можно передать переменную
        #'title': text,
        # А можно сразу записать значение в словарь. Но обычно так не делают
       # 'text': 'Главная страница'}
    return render(request, template) #context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
#def group_posts(request, slug):
   # return HttpResponse(f'Пост {slug}')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
