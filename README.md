TODO SPA
=======

Сервис событий, реализованный как SPA-приложение.
Пользователь создает событие (встреча, звонок и т.д.) с заголовком, 
содержанием и датой проведения. Пользователь имеет возможность 
совершать CRUD-операции над своими событиями. Искать по заголовку и фильтровать 
по дате (события за последние месяц, неделю, день).
За час до проведения события, сервис отправляет напоминание по e-mail автору.

Стек: Python3.6+, Django, DRF, vuejs, postgresql.

Настройки
------

Необходимо запускать решение в 3-х терминалах

####В терминале №1:

1 Загрузить конфиги в виде файла local.conf в директорию `./todo_api/conf/`. 
Все названия разделов и опций обязательны.
В конечном итоге должен получиться файл такого вида:

    [main]
    SECRET: <your django secret key>
    DEBUG: <boolean for debug status>
    
    [smtp]
    DOMAIN_NAME = <your domian name>
    EMAIL_HOST = <your email host>
    EMAIL_USE_TLS = <boolean for use TLS>
    EMAIL_PORT = <email port>
    EMAIL_HOST_USER = <email host user>
    EMAIL_HOST_PASSWORD = <email host password>
    
    [db]
    NAME: <database name>
    USER: <postgresql user name>
    PASSWORD: <postgresql user password>

2 Проинициализировать PostgreSQL

    $ export POSTGRES_DB=<database name from local.conf>
    $ export POSTGRES_USER=<postgresql user name from local.conf>
    $ export POSTGRES_PASSWORD=<postgresql user password from local.conf>
    $ sh prepare_db.sh
    
2 Подготовить виртуальное окружение для работы с бэкэндом

    $ source prepare_venv.sh
    
3 Перейти в директорию с бэкэндом и провести миграции джанго

    $ cd todo_api/
    $ python manage.py makemigrations
    $ python manage.py migrate

4 В директории бэкэнда запустить dev сервер джанго

    $ python manage.py runserver
    
####В терминале №2:

1 В корневой директории проекта активировать виртуальное окружение, 
перейти в директорию бэкэнда и запустить celery worker
    
    $ source venv/bin/activate
    $ cd todo_api/
    $ celery -A todo_api worker -B -l info


####В терминале №3:

1 Перейти из корневой директории проекта в директорию фронтэнда, установить менеджер
зависимостей npm, установить зависимости и запустить dev сервер
    
    $ cd todo_app/
    $ sudo apt install npm
    $ npm install
    $ npm run serve
    
2 Перейти по ссылке:

    http://localhost:8080/

