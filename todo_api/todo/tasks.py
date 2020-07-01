from __future__ import absolute_import, unicode_literals

from celery import shared_task

from todo.services import send_reminder_email


@shared_task
def send_reminder_email_task(*args):
    email, todo, *_ = args
    send_reminder_email(email, todo)
