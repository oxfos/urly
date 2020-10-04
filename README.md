## General

I used the Python package Django to create the web service (I don't know Flask yet).<br>
I use Python version 3.6.9 and pipenv (package for virtual environments).

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

### Set up

#### Assumptions:

- Python >= 3.6 is installed on your machine.

#### Steps:

- Clone/copy the source code to a local machine.
- If pipenv is not installed:

    $ pip install pip --upgrade     # to update and upgrade pip
    $ pip install pipenv

- Move inside the 'urly' directory (where Pipfile, .git etc. are) and create a virtual environment by typing-enter:
    
    $ pipenv install
 
This will install packages listed in `Pipfile` (if present).

If you don't use pipenv as virtual environment tool, probably you need `requirements.txt`.<br>
Use your standard tool for installing and launching a virtual environment and install packages by typing-enter:
    
    $ pip install -r requirements.txt


### Instructions to start the application

- Launch the virtual environment by moving inside the directory containing `Pipfile` and typing-enter:
    
    $ pipenv shell

- Move inside the directory containing the `manage.py` file and type-enter:
    
    $ python manage.py runserver

- The application is accessible at IP address 127.0.0.1, port 8000 ('localhost').

### Instructions to run unit tests

- Launch the virtual environment (see above).
- Move inside the directory containing the `manage.py` file and type-enter:
    
    $ python manage.py test

