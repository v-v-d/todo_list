from django.db import models

from authapp.models import TodoUser


class Todo(models.Model):
    name = models.CharField('todo name', max_length=64)
    text = models.CharField('todo text', max_length=512, blank=True)
    date = models.DateTimeField('todo date')
    timezone = models.CharField('todo timezone', max_length=128, blank=False)
    user = models.ForeignKey(TodoUser, related_name='todo_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
