# Тестовое задание ДенЛеДа

API книжного сервиса.

### Технологии

* python 3.10
* django 4.2
* djangorestframework 3.14
* djoser 2.2

### Установка

> Для развертывания и тестирования проекта необходимо установить [Docker](https://docs.docker.com/engine/install/)

- Клонируйте репозиторий:
```
git clone <link>
```

- Перейдите в папку `/app`, запустите сборку образа:
```
docker build -t denleda .
```

- Запустите проект:
```
docker run -it -p 8000:8000 denleda
```

### Доступные ресурсы

* http://localhost:8000/admin - админ-панель, доступ username `admin`, password `admin`
* http://localhost:8000/api/auth/token/login/ - авторизация и получение auth токена
* http://localhost:8000/api/auth/token/logout/ - логаут
* http://localhost:8000/api/books/ - GET/POST запросы к ресурсу книг
* http://localhost:8000/api/books/pk/ - GET/PUT/DELETE запросы к ресурсу книги

### Тестирование

Тесты описаны в `api/tests/`, для их запуска воспользуйтесь командой:
```
python manage.py test
```

### Автор

*Чупринский Станислав*
