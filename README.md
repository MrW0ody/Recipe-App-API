## In future I will add more complex readme

# Recipe-App-API

**This application is an advanced API project based on the Python language and Django REST
framework. The main purpose of the application is to enable users to authenticate, create,
update, and filter culinary recipes. Users can also upload and view images associated with the
recipes. Additionally, the application utilizes Docker containers for project management and a
Postgres database for data storage. An important aspect of the project is the implementation of
Test Driven Development approach and customization of the Django admin interface.**

# Installation

clone repository after this enter:

    docker-compose build

After this:

    dokcer-compose up

## to run tests:

    docker-compose run --rm app sh -c "python manage.py test"

go to address url:

    127.0.0.1:8000/api/docs

to create user go to address:

    127.0.0.1:8000/api/user/create

after creating user create token to authorize user, go to address:

    127.0.0.1/8000/api/user/token

after authorization test api by your own