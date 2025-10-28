## Flask + PostgreSQL + Marshmallow

This repo is a re-written "Tasks" CRUD API built with Flask Microframework. This time I used `SQLAlchemy` and the `psycopg2-binary` to attempt integration with a single-table Database in `PostgreSQL`, and of course, we use a lot of Flask-integrated libraries such as `requests`, `Blueprints`, `jsonify`, and plenty more.

The object serialization was built with `Marshmallow`, is a simplified object serialization library. This helps send and receive data between a server and a client.

## Pre-requisites

A virtualenv instance with Python selected executable

`virtualenv -p python3 venv`

Two databases were created for test and development environments. You can check the `config.py` file for more details about the connection string and the hardcoded placeholder name.

You will need to activate your virtual environment

## Creating a database from

Assuming you have a working default `PostgreSQL` service install, you can do the following:

```
> \c [database_name]
> CREATE TABLE [tasks]
```

You can verify the created tables using the `\dt` command.

## Installing pre-requisites

Locate the `requirements.txt` and `pip install -r requirements.txt`. Please be sure that you are using a Python3 Virtualenv instance. If not, some dependencies will break the project's normal behavior.
Be sure to start the PostgreSQL service. For macOS users, `Homebrew will be helpful

## Usage

Just. `python main.py`

## Prefix

The endpoint handling is done with `Flask Blueprints`, and for this project is the following
`[host]/api/v1/tasks`

## Unit test-cases

In the `test.py` exists, an extensive test-case suite exists for each verb of the HTTP functionality.

You can run it like this: `python test.py`

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
