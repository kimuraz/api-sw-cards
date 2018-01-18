# API server for Star Wars Cards
> Simple api server for fun and testing

## Install

```shell
$ pip install -r requirements.txt
```

## Setting database

```shell
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py loaddata cards.json
```

## Running server

```shell
$ ./manage.py runserver
```
