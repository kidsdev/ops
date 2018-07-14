Use Docker
==========

Install
-------

Clone

```
$ git clone -b master https://github.com/kidsdev/ops.git ops
$ echo -e "PORT=8080\nTAG=master" > ops/.env
```

or
```
$ git clone -b develop https://github.com/kidsdev/ops.git ops
$ echo -e "PORT=8080\nTAG=develop" > ops/.env
```

Run

```
$ cd ops
$ docker-compose up -d
$ docker-compose exec -T ops bash -c "python manage.py collectstatic --noinput"
$ docker-compose exec -T ops bash -c "python manage.py migrate"
```

Update
------

```
$ git pull
$ docker-compose pull
$ docker-compose up -d
$ docker-compose exec -T ops bash -c "python manage.py collectstatic --noinput"
$ docker-compose exec -T ops bash -c "python manage.py migrate"
```
