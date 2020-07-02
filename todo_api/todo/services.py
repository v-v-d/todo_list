import pytz
from django.core.mail import send_mail

from todo_api import settings


def send_reminder_email(email, todo_item):
    title = 'Your event will be soon.'
    name = todo_item.get('name')
    text = todo_item.get('text')

    timezone = todo_item.get('timezone')
    converted_date = todo_item.get('date').astimezone(pytz.timezone(timezone))
    date = converted_date.strftime("%d-%m-%Y %H:%M:%S")

    message = f'Name: {name}\nText: {text}\nDate: {date}'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False
    )
