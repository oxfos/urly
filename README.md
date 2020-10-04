## General

I used the Python package Django to create the web service (I don't know Flask yet).<br>
I use Python version 3.6.9 and pipenv (virtual environment package).

### Assumptions:

- `/shorten` is only to be used for POST (i.e. not for other request methods).
- The text next to error codes is the 'reason_phrase' (and not e.g. part of the body or else).
- The explanations are for a local, development server (not for e.g. production server).


### Possible improvements:
- Make a ShortcodeManager class to collect all shortcode utils functions in one place.
- Use other logic to produce unique shortcode when already many shortcodes are taken (random.sample() gets slower the less available combinations...).


## Details

### Source code

The source code can be downloaded from GitHub at https://github.com/Oxfos/urly.git

## Local set up

Assumptions:
- Python is installed on your machine.

Steps:
- Clone/copy the source code to a local machine.


### Set up virtual environment (I use pipenv)

- If pipenv is not installed:

    $ pip install pipenv # system wide

- Move to 'urly' project directory (where Pipfile, .git etc. are) and create virtual environment (it installs packages in Pipfile, if present):
    
    $ pipenv install


If you don't use pipenv probably you need requirements.txt:

- Install packages with requirements.txt:
    
    $ pip install -r requirements.txt


## Instructions to start the application

### Local

- Launch the virtual environment by moving to the directory containing `Pipfile` and typing-enter:
    
    $ pipenv shell

- Move to the directory containing the `manage.py` file and type-enter:
    
    $ python manage.py runserver

- The application is accessible at IP 127.0.0.1, port 8000 ('localhost').

## Instructions to run unit tests

- Launch the virtual environment (see above).
- Move to the directory containing the `manage.py` file and type-enter:
    
    $ python manage.py test



# Additional instructions

## Set up on production server

- install gunicorn:

    $ pipenv install gunicorn

- install production server, e.g. Nginx:
    
    $ 