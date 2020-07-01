from datetime import datetime

from django.core.mail import send_mail

from todo_api import settings


def send_reminder_email(email, todo_item):
    title = 'Your event will be soon.'
    name = todo_item.get("name")
    text = todo_item.get("text")
    date = datetime.strptime(todo_item.get("date"), "%Y-%m-%dT%H:%M:%SZ")

    message = f'Name: {name}\nText: {text}\nDate: {date}'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False
    )
