FROM python:3.6-alpine

EXPOSE 8000

COPY requirements.txt .
COPY manage.py .
COPY blog blog
COPY mysite mysite

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate && python manage.py loaddata users posts comments

ENTRYPOINT ["python", "manage.py", "runserver", "8000"]
