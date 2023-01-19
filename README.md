# fedor-js

## Python Virtual environment pipenv
run this to manage your project packages

'''
pipenv install 
pipenv shell

pipenv install <package name>
pipenv graph - to list installed packages

pipenv run pip freeze > requirements.txt
'''
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