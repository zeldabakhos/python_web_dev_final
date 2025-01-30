# Zelda and Galip's project

## Django Coding 

First we installed django. Created a virtual environment. Started a django project and app. From there, we added code in views.py, models.py, admin.py, created the serializers.py and adjusted settings.py depending on our use.

We decided to work on postgresql, created manually the student_management database, and used commands to create the tables. (python manage.py migrate)


## Accessing the backend

Then to access the localhost:

Make sure you are in the right folder and activated your virtual environment on which you installed all the required extensions (djangorestframework, django)

Run the following command in your terminal (in student_management folder) while in the project environment: python manage.py createsuperuser

It will ask for a username, an email, and a password (has to be more than 8 characters) the first time you access it.
You can now log in to the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.

Run this command: python manage.py runserver

To use the API simple change 'admin' to 'api' in the url.

PS: if you simply run the address in the terminal without '/admin/' or '/api' it might not work, so make sure to add it at the end of the url.

You will be able to add everything from the backend using the '/api/' addition


## Flask

The dash.html allows to show a table of  the students and their average grade.

To access this page, create a virtual environment in the 'project_to_fix' folder. Install flask and requests, and write the command 'flask run'.

PS: 'python manage.py runserver' and 'flask run' should be ran simultaneoulsy. It is best to use two different terminals in this case.

You should be set after that.