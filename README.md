## Overview

Lanbot.io API test
This flask application implements a REST API that will receive user data data (user name and email), store it on a DB and after 1 minute send a welcome email to the user. 

## Docker installation:

    $ docker build -t landbotio_users_api https://github.com/lusob/my-landbot-test-api.git
    $ docker run -p 5000:5000 my-landbot-test-api


## Locally installation

### To install it:

In the top-level directory:

    $ python3 -m venv env && source env/bin/activate
    $ pip install -r requirements.txt 

### To run it:

In the top-level directory:

    $ export FLASK_APP=main.py
    $ flask run

### To test it:

In the top-level directory:

    $ pytest

