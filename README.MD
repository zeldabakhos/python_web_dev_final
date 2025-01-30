# Zelda and Galip's project

## Django Coding 

First we installed django. Created a virtual environment. Started a django project and app. From there, we added code in views.py, models.py, admin.py, created the serializers.py and adjusted settings.py depending on our use.

We decided to work on postgresql, created manually the student_management database, and used commands to create the tables. (python manage.py migrate)

## Accessing the backend

Then to access the localhost:
Run the following command in your terminal (in student_management folder) while in the project environment: python manage.py createsuperuser

It will ask for a username, an email, and a password (has to be more than 8 characters) the first time you access it.
You can now log in to the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.

To use the API simple change 'admin' to 'api' in the url.

PS: if you simply run the address in the terminal without '/admin/' or '/api' it might not work, so make sure to add it at the end of the url.