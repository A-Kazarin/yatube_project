from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Post(models.Model):
    # Тип: TextField
    text = models.TextField()

    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.CASCADE)

class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название группы')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name= 'URL')
    description = models.TextField()

    def __str__(self):
        return self.title