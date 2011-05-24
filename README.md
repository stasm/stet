Stet is a simple blogging platform powered by git and django.

You push to a remote git repository which stores your posts in plain text 
files and a post-receive hook takes care of the rest:

- it converts the plain text to HTML using Markdown,
- it updates the database with the new HTML and meta data.

Installation
------------

1. Install `stet` with

    -e git+git://github.com/stasm/stet.git#egg=stet

2. Add `stet` and the dependencies to `INSTALLED_APPS`


    INSTALLED_APPS = (

        # ...your other apps go here...

        'django.contrib.comments',
        'taggit',
        'stet',
    )

3. Enable the meta-data extension for Markdown by editing your settings.py file 
   and adding the following setting:

    MARKDOWN_EXT = (
        'meta',
    )

    You can also add other extensions as well, if you wish, for instance:

    MARKDOWN_EXT = (
        'meta',
        'abbr',
        'def_list',
        'fenced_code',
        'footnotes',
        'headerid',
    )

4. Copy `hooks/post-receive` into the `hooks` directory of the remote 
   repository in which you store your posts.

5. Configure the `ROOT` variable in the `post-receive` hook to match the root of 
   your Django project (the directory in which `manage.py` is located).
