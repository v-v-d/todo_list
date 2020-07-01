from django.core.mail import send_mail

from todo_api import settings


def send_reminder_email(email, todo_item):
    title = f'You have an event scheduled'
    message = f'Name: {todo_item.name}\nText: {todo_item.text}\nDate: {todo_item.date}'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False
    )
