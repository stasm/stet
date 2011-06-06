from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site

from stet.models import Article

class ArticleFeed(Feed):
    @property
    def site(self):
        if not hasattr(self, '_site'):
            self._site = Site.objects.get_current()
        return self._site

    def title(self):
        return ("%s - Articles") % self.site.name

    def link(self):
        return "http://%s/" % self.site.domain

    def description(self):
        return "Latest articles on %s" % self._site.name

    def items(self):
        return Article.live.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract
