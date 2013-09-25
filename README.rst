========================
django-template-heroku
========================

This project is based on Django 1.5 TwoScoops Project (https://github.com/twoscoops/django-twoscoops-project)
and adapted to Heroku. There are a few changes listed below:

#. Bootstrap 2 replaced with Bootstrap 3.
#. base.py and other setting files are same with TwoScoops. heroku.py added.
#. Repository and Project root directories are same to avoid extra settings.
#. Heroku dependencies are added to heroku.txt. Heroku tutorial (https://devcenter.heroku.com/articles/getting-started-with-django) followed for adapting.
#. If an  environment variable exists HEROKU=true, heroku.py will be used for settings. Otherwise default local settings will be used. If you want to add other options check manage.py and wsgi.py for settings.

Creating your project at local
==============================

We need a virtual environment. You can create with virtualenv or virtualenvwrapper::

    # with virtualenvwrapper
    $ mkvirtualenv dth
    # or with virtualenv
    $ virtualenv dth && source dth/bin/activate

Be sure that your virtual environment is activated.

Installation of Dependencies
----------------------------

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt/production.txt

To create a new Django project called '**your_project_name**' using
django-template-heroku, run the following command::

    $ django-admin.py startproject --template=https://github.com/sercanu/django-template-heroku/archive/master.zip --extension=py,rst,html --name=Procfile your_project_name
    # After creating project you can run it
    $ cd your_project_name
    $ python manage.py runserver
    # Now you can visit the main page.
    # syncdb for admin page
    $ python manage.py syncdb
    .....
    .....
    # After creating superuser account, you can login to /admin

Creating your project at Heroku
================================

To create a new Django project called '**your_project_name**' using
django-template-heroku, run the following command::

    $ django-admin.py startproject --template=https://github.com/sercanu/django-template-heroku/archive/master.zip --extension=py,rst,html --name=Procfile your_project_name
    $ git init
    $ git add .
    $ git commit -m "initial commit"
    $ heroku create
    $ heroku apps:rename yourprojectname # This is optional
    $ heroku config:add HEROKU=true # This is must
    $ git push heroku master
    .....
    .....
    # After push complete you can visit main page
    $ heroku open
    # syncdb for admin page
    $ heroku run python manage.py syncdb
    .....
    .....
    # After creating superuser account, you can login to /admin


Notes
================================

Secret Key for Security
-----------------------

Add SECRET_KEY parameter to heroku.py like production.py for security. After getting SECRET_KEY from environment you should add heroku config::

    $ heroku config:add SECRET_KEY=...your secret key ...

Site matching query does not exist error
----------------------------------------

Normally your site will have ID = 1 when creating it at first time. Default value of SITE_ID is 1 also at settings.
But sometimes, for example when an error occurs while creating the superuser, site record may have not been created. This is the root of error. You can fix it like below:
(http://stackoverflow.com/questions/11814059/site-matching-query-does-not-exist)


