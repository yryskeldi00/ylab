# web-сервис

# Описание проекта

web-сервис

# Как поднять локально проект?

Зависимости:

- PostgreSQL
- Python 3.9
- Django 3.2
- python 3.9
- djangorestframework 3.13.1
- drf-yasg 1.20.0
- django-environ 0.8.1
- psycopg2-binary 2.9.3


## Переменные окружения для продакшена, для локальной разработки можно и не указывать:

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | secret key  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DJANGO_ALLOWED_HOST`| Allowed host | 0.0.0.0,127.0.0.1 |

## Последовательность действий 

```.bash
    $ git clone https://gitlab.com/Yryskeldi/ylab.git
    $ cd ylab/ 
    $ docker-compose build
    $ docker-compose run lab_task python manage.py migrate
    $ docker-compose up
```

Если все успешно то переходите по ссылке ==> `http://0.0.0.0:8000/docs/`


## Последовательность действий без докера

```.bash
    $ https://gitlab.com/Yryskeldi/ylab.git
    $ cd ylab/ 
    $ poetry install
    $ poetry shell
```

После создания БД, необходимо применить миграцию, после запуск тестового
сервера:

```.bash
    $ python manage.py migrate
    $ python manage.py runserver
```

Если все успешно то переходите по ссылке ==> `http://locahost:8000`
