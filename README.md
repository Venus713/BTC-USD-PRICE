# BTC/USD-PRICE

## Pre-requisites

- Python 3.8
- Virtualenv
- PostgreSQL
- Redis

## Git Clone Project

    ```bash
    git clone git@github.com:TripElephant/mobytrip-hotelbeds.git
    ```

## Locally Run

### Create DB

    ```bash
    $ sudo -u postgres psql
    postgres=# CREATE DATABASE <your-db-name>;
    postgres=# CREATE USER <your-username> WITH PASSWORD '<your-password>';
    postgres=# ALTER ROLE <your-username> SET timezone TO 'UTC';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE "<your-dbname>" to <your-username>;
    ```

### Env configuration

    - Copy/Past `.env` from `.env.dev` file.

        ```bash
        cp .env.example .env
        ```

    - And pleae edit the env variables in the `.env`.

### Install requirements

    ```bash
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements/development.txt
    ```
    or
    ```bash
    pip install -r requirements/production.txt
    ```

### Setting Django Enviroment

    ```bash
    $ export DJANGO_SETTING_MODULE=config.settings.development
    ```
    or
    ```bash
    $ export DJANGO_SETTING_MODULE=config.settings.production
    ```

### Run

    - run django project

        ```bash
        $ python manage.py migrate
        $ python manage.py runserver
        ```

    - run scheduler:

        In order to start the `celery worker`, open another terminal, and run following command.

        ```
        $ celery -A config worker -l INFO
        ```

        Also, in order to start the `celery beat`, open another terminal,

        ```
        $ celery -A config beat -l INFO
        ```

## Docker Run

### Docker Env configuration

    - Copy/Past `.env` from `.env.docker` file.

        ```bash
        cp .env.example .env.docker
        ```

    - And pleae edit the env variables in the `.env.docker`.

### Docker build/rebuild and run

    ```bash
    $ docker-compose up --build
    ```
    or
    ```bash
    $ make build
    $ make rebuild
    $ make run
    $ make down
    ```
