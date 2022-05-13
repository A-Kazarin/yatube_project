from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField(verbose_name= 'Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name= 'Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Автор')
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.CASCADE, verbose_name= 'Сообщество')

class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название группы')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name= 'Адрес')
    description = models.TextField(verbose_name= 'Описание')

    def __str__(self):
        return self.title