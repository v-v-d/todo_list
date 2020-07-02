from datetime import datetime

import pytz
from django.core.mail import send_mail

from todo_api import settings


def send_reminder_email(email, todo_item):
    title = 'Your event will be soon.'
    name = todo_item.get('name')
    text = todo_item.get('text')
    date = get_valid_date(todo_item.get('date'), todo_item.get('timezone'))

    message = f'Name: {name}\nText: {text}\nDate: {date}'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False
    )


def get_valid_date(str_date, timezone):
    date_obj = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%SZ')
    converted_date = date_obj.astimezone(pytz.timezone(timezone))
    return converted_date.strftime("%d-%m-%Y %H:%M:%S")
