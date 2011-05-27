import sys
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from stet.models import Article

class Command(BaseCommand):
    args = 'FILENAME -'
    option_list = BaseCommand.option_list + (
        make_option('--replaces', '-r', default=None, dest='oldname',
                    help='The name of the file this file replaced.'),
    )

    help = 'Record the new contents of a file called FILENAME in the ' \
           'database.  The contents are read from the STDIN.'

    def handle(self, filename, **options):
        if not filename:
            raise CommandError('Specify a filename')

        sys.stdout.write('Recording the contents of %s\n' % filename)

        # if this is a rename, look for the old name in the DB
        oldname = options['oldname'] or filename
        try:
            article = Article.objects.get(filename=oldname)
        except Article.DoesNotExist:
            article = Article(filename=filename)
            sys.stdout.write('  ..created a new article\n')
        else:
            sys.stdout.write('  ..found an existing article\n')
            if oldname != filename:
                sys.stdout.write('    ..previously called %s\n' % oldname)
                article.filename = filename
        article.body = sys.stdin.read()
        article.save()

        sys.stdout.write('  ..done.\n')
