from django.db import models
from django.utils import timezone

from authapp.models import TodoUser


class Todo(models.Model):
    name = models.CharField('todo name', max_length=64)
    text = models.CharField('todo text', max_length=512, blank=True)
    date = models.DateTimeField('todo date')
    created = models.DateTimeField('todo created date', default=timezone.now())
    is_active = models.BooleanField('todo active status', db_index=True, default=True)
    user = models.ForeignKey(TodoUser, related_name='todo_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def is_date_expired(self):
        return self.date < timezone.now()
