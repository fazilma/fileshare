# fileshare
 
How to Run

This is a django project with docker containerization. This will run as django project as well

The docker way is

1. install docker 
2. run the command docker-compose up
3. The program should be up

As independent Django Project

1. once django is installed
2. install virtual env
3. run the command pip install -r reuirements.txt
4. run python manage.py makemigrations
5. run python manage.py migrate
6. run python manage.py runserver

once the program is up 
create a superuser // https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user

then go to 12.0.0.1:8000/admin
enter the user name and password created for the superuser,
once logged in as a super user, create users

then go to 12.0.0.1:8000/ 
start using the app


