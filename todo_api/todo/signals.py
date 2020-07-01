from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from todo.models import Todo
from todo.tasks import send_reminder_email_task


@receiver(post_save, sender=Todo)
def start_send_reminder_email_task(sender, instance, **kwargs):
    todo_date = sender.get_item(instance.date)
    reminder_date = todo_date - timezone.timedelta(hours=1)
    user_email = sender.get_item(instance.user.email)

    send_reminder_email_task(user_email, instance).apply_async(eta=reminder_date)
