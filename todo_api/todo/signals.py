from celery.worker.control import revoke
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.utils import timezone

from todo.models import Todo
from todo.tasks import send_reminder_email_task


@receiver(post_save, sender=Todo)
def start_send_reminder_email_task(sender, instance, **kwargs):
    todo_date = instance.date
    reminder_date = todo_date - timezone.timedelta(hours=1)
    user_email = instance.user.email
    todo_item = model_to_dict(instance)

    if instance.task_id:
        revoke(instance.task_id, terminate=True, signal='SIGKILL')

    task_id = send_reminder_email_task.apply_async(
        args=[user_email, todo_item], eta=reminder_date
    )

    instance.task_id = task_id
    # instance.save()
