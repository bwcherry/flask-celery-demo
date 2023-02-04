# flask-celery-demo

This is a demo project that shows the basics around getting celery, flask, and redis working together. This expands on an approach that is labeled as **Application Factories** in the flask documentation by adding Celery.
https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/

## Notes

I tested this running on Windows 10 Home version 22H2 running under Docker Desktop for Windows.

## Prerequisites

### Install Docker
https://docs.docker.com/engine/install/

## Download Code

Look for the green button that says **Code** and click on it. You should see a new list of options displayed. Look for the text **Download ZIP** and click on it. Your browser should begin downloading the zip file. Once that completes, extract the zip file.

## Open Command Prompt

Open the newly extracted folder with Windows Explorer. You will be in the correct folder if you see a file labeled **README.md**. Press `Alt + D`, type `cmd` and press `Enter`. If you followed along so far you should have a command prompt opened to the correct path we need to start using **Docker Compose**.

## Setup .env File

Type `copy env-example.txt .env` and press `Enter`.

## Down The Rabbit Hole

It is important to explain what is going to happen before we run the next command. The first thing that docker will do is look for a file named `docker-compose.yml` in the current directory. Once it reads the file, it will begin checking to see if you have all of the images we need to run all of the containers. If it does not find an image that we need, it will begin downloading them from **dockerhub.com**. Once all of the images have been downloaded, it will then work on building our custom flask image. This involves setting up a virtual environment and installing our required packages with pip. Once that all finishes it will begin bringing up the containers. You will see the log messages that are prefixed with the container that generated the message. It might take some time for things to settle down, but you will know it has completed when you can access the flask development website.

## Run Docker Compose

When you are ready to begin, type `docker compose up` and press `Enter`.

## Accessing Flask

Open up a browser and type in `localhost:5000`. If you don't see anything immediately, you might need to give the containers time to begin communicating with each other. Give it a few seconds and then try the refresh button. If you continue to have problems, take a look over the logs to try to find out where the problem lies.

## Run The Demo

Run the website through its paces by adding/deleting a few users. If you can arrange your windows where you can view the website and the console logs at the same time. This should give you an idea of how your actions on the website affect the containers.

## Stopping The Containers

Make sure you have the command prompt activated and press `Ctrl + C`. You should see the containers begin to react by shutting down. I will include the links below if you want to checkout more information about docker.

### Basic Overview
https://docs.docker.com/compose/

## The Journey Awaits

Try tinkering around. It could be something like adding in an **edit feature**. You could try modifying it to use **WTForms** or integrating **Flask-Login**. I did not create this to be a completed project. This was just to help you get your feet wet.
