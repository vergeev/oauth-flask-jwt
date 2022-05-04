# oauth-flask-jwt

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A training project for building an OAuth API authnentication using a jwt token.

Follows [this tutorial](https://github.com/grizzlypeaksoftware/flask-auth-service#synopsis).

As a way to spin-up Postgres, I used [this tutorial](https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f).

Developer dependencies, such as linters and formatters, are managed by [pre-commit](http://pre-commit.com).

In order to run the project, do `flask run` inside your virtual environment.
Flask [will load](https://flask.palletsprojects.com/en/2.1.x/cli/#environment-variables-from-dotenv) the environment variables from the dotenv automatically.
