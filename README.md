Use Docker
==========

Install
-------

```
$ echo "PORT=8080" > .env
$ docker-compose up -d
$ docker-compose exec -T ops bash -c "python manage.py collectstatic --noinput"
$ docker-compose exec -T ops bash -c "python manage.py migrate"
```

Update
------

```
$ docker-compose pull
$ docker-compose up -d
$ docker-compose exec -T ops bash -c "python manage.py collectstatic --noinput"
$ docker-compose exec -T ops bash -c "python manage.py migrate"
```
