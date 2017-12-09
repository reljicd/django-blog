# Django Blog Demo

## About

This is a demo project for practicing Django.
The idea was to build some basic blogging platform.

It was made using Python 3.6 and Django 
Database is SQLite.

There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts. 
Every authenticated user can comment on posts made by other users.
Home page is paginated list of all posts.
Non-authenticated users can see all blog posts, but cannot add new posts or comment.

## Configuration

\[Optional\] Install virtual environment:

```bash
python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
source env/bin/activate
```

On Windows:
```bash
.\env\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```

Initialize data:
```bash
python manage.py loaddata users posts comments
```

## How to run

You can run the application from the command line with manage.py.

Go to the root folder of the application and type:
```bash
$ python manage.py runserver
```

Go to the web browser and visit `http://localhost:8000/home`

Admin username: **admin**

Admin password: **adminpassword**

User username: **dusan**

User password: **dusanpassword**

## Helper Tools

### Django Admin

It is possible to add additional admin user who can login to the admin site. Run the following command:
```bash
python manage.py createsuperuser
```
Enter your desired username and press enter.
```bash
Username: admin_username
```
You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```bash
Password: **********
Password (again): *********
Superuser created successfully.
```

Go to the web browser and visit `http://localhost:8000/admin`

