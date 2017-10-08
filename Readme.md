## Set mutiple settings in diffirent environments

Move the settings.py to `settings` folder and rename as `base.py`

And create the following new files for development/production environments.
1. dev.py
2. prod.py

> Move the follwoing settings to `dev.py` and `prod.py`.
> 
>* SECRET_KEY = '!&r6$4bw+yhf6_+z0bfay%t%s051e=!*0kii0+dev_5!wwea46'
>* DEBUG = True
>* ALLOWED_HOSTS = ['*']

*dev.py

```
SECRET_KEY = 'XXXXXXXX'
DEBUG = True
ALLOWED_HOSTS = ['*']
```

*prod.py

```
SECRET_KEY = 'yyyyyyyyyy'
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

> Notice that when DEBUG is disabled, the `ALLOWED_HOSTS` is required.



## Modify BASE_DIR

While we move the settings file to `/settings`, we have to modify the `BASE_DIR` as following.

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
```


## Enable admin

### Run Auth migration

```
$ python manage.py migrate auth
```

### Update settings.py

* Original 

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #...
]
```

* After update

```
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #...
]
```


### Create super user

```
$ python manage.py createsuperuser
```



### Trouble shootings

1. `WSGIRequest` object has no attribute 'user' Django admin

* Error message
> "WSGIRequest" object has no attribute 'user' Django admin

Go to settings.py and replace `MIDDLEWARE=[...]` with  `MIDDLEWARE_CLASSES=[...]`.

Reference: [Stackoverflow](https://stackoverflow.com/questions/37949198/wsgirequest-object-has-no-attribute-user-django-admin)

2.  django_session not exists

* Error message 
> (-2147352567, '發生例外狀況。', (0, 'Microsoft OLE DB Provider for SQL Server', "無效的物件名稱 'django_session'。", None, 0, -2147217865), None) 
> Command: SELECT (1) AS [a] FROM [django_session] WHERE [django_session].[session_key] = ? ORDER BY 1 OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY

Try migrate the database again with `$ python manage.py migrate`

Reference : [Stackoverflow](https://stackoverflow.com/questions/39706062/django-db-utils-programmingerror-relation-django-session-does-not-exist-line)



