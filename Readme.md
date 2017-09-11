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
