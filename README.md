Stet is a simple blogging application powered by git and django.

You push to a remote git repository which stores your posts in plain text 
files and a post-receive hook takes care of the rest:

- it converts the plain text to HTML using Markdown,
- it updates the database with the new HTML and meta data.

Then, `stet` serves the blog posts via django, adding some nice feature, like 
tagging and comments.

Installation
------------

1. Install `stet`:

        pip install -e git+git://github.com/stasm/stet.git#egg=stet

1. Install the dependencies:

        pip install -r https://github.com/stasm/stet/raw/master/requirements.txt

1. Add `stet` and the dependencies to `INSTALLED_APPS`.  Make sure you list the 
   dependencies _after_ `stet`:

        INSTALLED_APPS = (

            # ...your other apps go here...

            'stet',
            'django.contrib.comments',
            'taggit',
        )

1. Enable the meta-data extension for Markdown by editing your settings.py file 
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
            'downheader',
        )

1. Copy `hooks/post-receive` into the `hooks` directory of the remote 
   repository in which you store your posts.

1. Configure the `ROOT` variable in the `post-receive` hook to match the root of 
   your Django project (the directory in which `manage.py` is located).
