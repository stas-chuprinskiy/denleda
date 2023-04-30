FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py loaddata fixtures.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
