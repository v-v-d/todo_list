from __future__ import absolute_import, unicode_literals

from celery import shared_task

from todo.services import send_reminder_email


@shared_task
def send_reminder_email_task(email, todo_item):
    send_reminder_email(email, todo_item)
