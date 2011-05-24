import sys

from django.core.management.base import BaseCommand, CommandError

from stet.models import Article

class Command(BaseCommand):
    args = 'FILENAME -'

    help = 'Records the new contents of a file called FILENAME in the ' \
           'database.  The contents are read from the STDIN.'

    def handle(self, filename, files, **options):
        if not filename:
            raise CommandError('Specify a filename')
        try:
            article = Article.objects.get(filename=filename)
        except: 
            article = Article(filename=filename)
        article.body = sys.stdin.read()
        article.save()
