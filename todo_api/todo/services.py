from django.core.mail import send_mail

from todo_api import settings


def send_reminder_email(email, todo_item):
    title = f'You have an event scheduled'
    name = todo_item.get("name")
    text = todo_item.get("text")
    date = todo_item.get("date")

    message = f'Name: {name}\nText: {text}\nDate: {date}'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False
    )
