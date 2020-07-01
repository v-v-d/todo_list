from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from todo.models import Todo
from todo.tasks import send_reminder_email_task


@receiver(post_save, sender=Todo)
def start_send_reminder_email_task(sender, instance, **kwargs):
    todo_date = instance.date
    reminder_date = todo_date - timezone.timedelta(minutes=1)
    user_email = instance.user.email

    send_reminder_email_task.apply_async(
        email=user_email, todo=instance, eta=reminder_date
    )
