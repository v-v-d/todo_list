from __future__ import absolute_import, unicode_literals

from celery import shared_task

from todo.services import send_reminder_email


@shared_task
def send_reminder_email_task(**kwargs):
    send_reminder_email(kwargs.get('email'), kwargs.get('todo'))
