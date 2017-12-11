FROM python:3.6-alpine

EXPOSE 8000

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project files
COPY manage.py .
COPY blog blog
COPY mysite mysite

# Run migrations, and load the database with fixtures
RUN python manage.py migrate && python manage.py loaddata users posts comments

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
