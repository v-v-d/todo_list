from celery import current_app
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.utils import timezone

from todo.models import Todo
from todo.tasks import send_reminder_email_task


@receiver(pre_save, sender=Todo)
def start_send_reminder_email_task(sender, instance, **kwargs):
    todo_date = instance.date
    reminder_date = todo_date - timezone.timedelta(hours=1)
    user_email = instance.user.email
    todo_item = model_to_dict(instance)

    current_todo_item = sender.objects.filter(pk=instance.pk).first()
    if current_todo_item:
        current_date = current_todo_item.date

        if current_date != todo_date:
            current_app.control.revoke(
                task_id=instance.task_id, terminate=True, signal='SIGKILL'
            )

    task_id = send_reminder_email_task.apply_async(
        args=[user_email, todo_item], eta=reminder_date
    )

    instance.task_id = task_id


@receiver(pre_delete, sender=Todo)
def kill_reminder_email_task(sender, instance, **kwargs):
    if instance.task_id:
        current_app.control.revoke(
            task_id=instance.task_id, terminate=True, signal='SIGKILL'
        )
