django-rax
==========

[![Build Status](https://travis-ci.org/dustinfarris/django-rax.png?branch=master)](TravisCI)

Django-rax is an implementation of 
[pyrax](http://github.com/rackspace/pyrax.git) for Django that allows
you to synchronize your static files with Rackspace Cloud Files.
Also included is an optional storage backend for your media files.

This project is **under development** and should not be used in a
production environment.

Installation
------------

Install via pip:

```sh
$ pip install django-rax
```

Add ``rax`` to your INSTALLED_APPS. If you want to use the storage
backend for your media files, add this to settings.py:

```python
DEFAULT_FILE_STORAGE = 'rax.storage.RaxStorage'
```

Configuration
-------------

You will need to provide your Rackspace credentials (username, and API
key). These can be obtained from the "mycloud" control panel.

```python
RAX = {
  'USERNAME': 'yourusername',
  'API_KEY': 'yourapikey',
  'REGION': 'ORD',
  'CONTAINER': 'yourcontainer'}
```

"REGION" can be one of ORD, DFW, or LON. If this is not specified, it
will default to Chicago (ORD).

Media files are uploaded to the root of your container, and static
files will be prefixed by the base name of your STATIC_ROOT setting; 
for example, if your STATIC_ROOT is /Users/me/myproject/static/, then
your static files will be prefixed with 'static/'. That being said,
your STATIC/MEDIA URL settings should look something like:

```python
STATIC_URL = 'http://mycdncname.mydomain.com/static/'
MEDIA_URL = 'http://mycdncname.mydomain.com/'
```

Django Compressor
-----------------

If you use django-compressor, you will need to turn on the compress
offline to ensure the compressed files are available for syncing.

```python
COMPRESS_OFFLINE = True
```

Help
----

Email any questions to
[dustin@dustinfarris.com](mailto:dustin@dustinfarris.com) or report
[issues on GitHub](https://github.com/dustinfarris/django-rax/issues)
