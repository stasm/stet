from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

from markdown import Markdown

class Article(models.Model):
    filename = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=150)
    excerpt = models.TextField()
    body = models.TextField()
    html = models.TextField()

    objects = models.Manager()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        md = Markdown(extensions=settings.MARKDOWN_EXT)
        self.html = md.convert(self.body)
        m = md.Meta
        self.title = ' '.join(m.get('title', []))
        self.excerpt = ' '.join(m.get('excerpt', []))
        super(Article, self).save(*args, **kwargs)
        self.tags.add(*m.get('tags', []))
