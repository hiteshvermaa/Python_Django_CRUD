# Python_Django_CRUD


This is a small Django project to demonstrate Django CRUD functionality, it
consist of 3 small applications:

- Attendence_Class_base_view: Implement CRUD using Class Based Views.
- Attendence_Function_base_view: Implement CRUD using Function Based Views.
- Attendence_Function_base_view_user: add user interaction to Attendence_Function_base_view example.

This project need a single python package "Django" use the command below to install:

    pip install -r requirements.txt

Before running the application we need to create the needed DB tables:

    python ./manage.py migrate

Now you can run the development web server:

    python ./manage.py runserver

To access the applications go to the URL "http://localhost:8000/"

you do need to create a user to test it, you can create a user using the following command:

    python ./manage.py createsuperuser

To create a normal user (non super user), you must login to the admin page and
create it: <http://localhost:8000/admin/>
