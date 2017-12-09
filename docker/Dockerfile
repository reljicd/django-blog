FROM python:3.6-alpine

EXPOSE 8000

COPY requirements.txt .
COPY mysite mysite

RUN pip install --no-cache-dir -r requirements.txt

RUN python mysite/manage.py migrate && python mysite/manage.py loaddata users posts comments

ENTRYPOINT ["python", "mysite/manage.py", "runserver", "8000"]
