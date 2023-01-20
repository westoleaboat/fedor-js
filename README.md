# Boilerplate for hosting a Flask app in [render.com](https://www.render.com)

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
