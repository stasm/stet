import sys

from django.core.management.base import BaseCommand, CommandError

from stet.models import Article

class Command(BaseCommand):
    args = 'FILENAME'

    help = 'Remove the file called FILENAME from the database.'

    def handle(self, filename, **options):
        if not filename:
            raise CommandError('Specify a filename')

        sys.stdout.write('Removing %s\n' % filename)

        try:
            Article.objects.get(filename=filename).delete()
            sys.stdout.write('  ..done.\n')
        except: 
            sys.stdout.write('  ..FAILED.\n')
