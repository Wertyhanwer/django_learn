from django.db import models

class AppTest(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True) # Этот параметр разрешает null.
    time_create = models.DateTimeField(auto_now_add=True) # Автоматически заполняет поле при создании дефолтным значением, здесь это текущее время.
    time_update = models.DateTimeField(auto_now=True) # Будет менять поле каждый раз когда меняется эта запись в бд
    is_published = models.BooleanField(default=True)
    id = models.IntegerField(primary_key=True)