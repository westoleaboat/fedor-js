# Boilerplate for hosting a Flask app in [render.com](https://www.render.com)
The aim is to get a JSON payload when accesing a URL.
You will render your project repository, it will contain the following *initial* structure:

|File|Description|
|---------|-----|
|.flaskenv|FLASK environment variables|
|.gitignore|local files you dont need/want to share|
|app.py|main app config|
|docker-entrypoint.sh|entrypoint for rendering application|
|Dockerfile|environment for your web service|
|Pipfile|from local virtual environment|
|Pipfile.lock|from local virtual environment|
|README.md|This file|
|requirements.txt|Python packages needed to run app|
|settings.py|project settings, not sure I need this here|

![Screenshot_select-area_20230120131120](https://user-images.githubusercontent.com/68698872/213681575-72a58b47-c072-440f-a3e0-7fcbf32a04e6.png)
## Prepare your working environment
Go to your project folder and git clone this repository, then activate your virtual environment. 
There is many ways and I use pipenv, you can use anything you want. dont forget to install required packages

with pip:
```
$ python3 -m venv ./venv            # create environemnt
$ source ./venv/bin/activate        # activate your environment
$ pip install -r requirements.txt   # install required packages
```
with pipenv

```
$ pipenv install                     # create environemnt
$ pipenv shell                       # activate your environment
$ pipenv install -r requirements.txt # install required packages
```
how to list installed packages
```
pip freeze   # with pip
pipenv graph # with pipenv
```
how to create requirements.txt
```
pip freeze > requirements.txt            # from pip
pipenv run pip freeze > requirements.txt # from pipenv
```



~~pipenv install flask~~

git push your changes to your project repository. Render will work with the last commit.


to proceed you can register in render.com and create a new Web Service
![Screenshot_select-area_20230120130007](https://user-images.githubusercontent.com/68698872/213679528-c5d1c3c0-174f-4649-8efa-048ba0582f8c.png)

Connect your repository
![Screenshot_select-area_20230120132843](https://user-images.githubusercontent.com/68698872/213684676-38648b45-8c2a-4302-bb78-e2f61224d7cb.png)

## Build & Deploy
In render.com, The runtime **environment** for your web service is a **Dockerfile**.
![Screenshot_select-area_20230120125337](https://user-images.githubusercontent.com/68698872/213678389-0fe0e4ab-39f4-4dac-95b9-b6a92f518980.png)

## Why a Dockerfile?
![Screenshot_select-area_20230120130804](https://user-images.githubusercontent.com/68698872/213681085-4583feff-32cb-418b-8288-2ec9d5501156.png)

A Dockerfile is a set of instructions for the virtualization of your project when being hosted. 

## Still missing
- [ ] Run Project locally
- [ ] Add elephantSQL database

## To run this project locally
create a virutal environment in your project folder. (either pip or pipenv works)

```
pipenv install # create environemnt
pipenv shell   # activate your environment

pipenv install -r requirements.txt # to install required packages
pipenv graph                       # list installed packages
```
how to create a requirements.txt from pipenv 
```
pipenv run pip freeze > requirements.txt
```
pipenv install flask

create app.py

##Anatomy of a Flask route
There are two parts to a Flask route:

The endpoint decorator
The function that should run
The endpoint decorator (@app.get("/store")) registers the route's endpoint with Flask. That's the /store bit. That way, the Flask app knows that when it receives a request for /store, it should run the function.

The function's job is to do everything that it should, and at the end return something. In most REST APIs, we return JSON, but you can return anything that can be represented as text (e.g. XML, HTML, YAML, plain text, or almost anything else).

https://rest-apis-flask.teclado.com/docs/first_rest_api/what_is_json/

write Dockerfile
https://rest-apis-flask.teclado.com/docs/docker_intro/run_docker_container/
