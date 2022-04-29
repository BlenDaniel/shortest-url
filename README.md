# Short.est - Link Generator

# Introduction

This is a simple url shortner. I will try to do UI for it but as of now, priority is just to send and recieve JSON formated requests and response bodies.
<br>
To give you a breif overview of what I will be doing: Creating a table to store the long urls with a respective replacement urls. When a user calls the API, they can get a shortend URL that will redirect them to the original URL.
Since the requirement asks for not persisiting to store the short URLs to a database and rather keep them in memory, I will implement a Redis cache with Flask for that particular approach. 
<br>
Redis is a key/value style in memory database for caching web applications and reducing overall page load times. Please follow the installation guides for setting up Redis on your machine.

# Installation Guides

For the proper functioning of the application, you need to have python3 and pip installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
<br>
For installing of our caching mechanism, you can follow the installation guide [here](https://redis.io/docs/getting-started/installation/) and install Redis. 
<br>
For specific JSON request-reponse testing, Download Postman [here](https://www.postman.com/downloads/)<br>
<br>

# Procedure for running the flask-app
### Install a virtual machine

    pip3 install pipenv

Once it's installed, you can create a virtual environment and activate it using this command:

### Start the virtual environment.

    pipenv shell
###  To deactivate the virtual environment, you can use this command:

    exit
### Install all the dependencies

    pipenv install -r requirements.txt


Once all the packages are installed, run the following command in the same command line.

## For starting the Redis Service
### For mac

    brew services start redis
### For linux

    sudo systemctl start redis

### For linux to automatically start Redis when your server boots

    sudo systemctl enable redis
### For windows

    Open Run Window by Winkey + R
    Type services.msc
    Search Redis service
    Click stop, start or restart the service option.

## For stopping the Redis Service

### For mac

    brew services stop redis
### For linux

    sudo systemctl restart redis
### For windows

    Open Run Window by Winkey + R
    Type services.msc
    Search Redis service
    Click stop, start or restart the service option.

## For Restarting the Redis Service

### For mac

    brew services restart redis
### For linux

    sudo systemctl restart redis
### For windows

    Open Run Window by Winkey + R
    Type services.msc
    Search Redis service
    Click stop, start or restart the service option.

## For running the flask app
### For mac and linux

    export FLASK_APP=run.py
    flask run
### For windows

    set FLASK_APP=run.py
    flask run

### Create a ```.env``` file in the root with the following parameters
    SECRET_KEY=secretkey
    DATABASE_URL=sqlite:///shortest.db
    APP_SETTINGS=config.DevelopmentConfig
    FLASK_APP=core

Then, open http://127.0.0.1:5000/ in your web browser to view our application.

# Tests
To run the test cases, you need to be in the virtual environment and also have your cache system running. 
<br>

## For starting the virtual environment.

    pipenv shell

## For starting the Redis Service (Cache memory)
### For mac

    brew services start redis
### For linux

    sudo systemctl start redis

### For linux to automatically start Redis when your server boots

    sudo systemctl enable redis
### For windows

    Open Run Window by Winkey + R
    Type services.msc
    Search Redis service
    Click stop, start or restart the service option.

### To run tests:

    python core/tests/test_basic.py

