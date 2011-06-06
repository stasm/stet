from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse

from stet.models import Article

class SiteFeed(Feed):
    @property
    def site(self):
        if not hasattr(self, '_site'):
            self._site = Site.objects.get_current()
        return self._site


class ArticleFeed(SiteFeed):
    def title(self):
        return ("%s - Articles") % self.site.name

    def link(self):
        return "http://%s/" % self.site.domain

    def description(self):
        return "Latest articles on %s" % self.site.name

    def items(self):
        return Article.live.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract


class CommentsForArticleFeed(SiteFeed):
    def get_object(self, request, article_id):
        return get_object_or_404(Article, pk=article_id)

    def title(self, article):
        return ("Comments on %s - %s") % (self.site.name, article.title)

    def link(self, article):
        return "http://%s%s" % (self.site.domain, article.get_absolute_url())

    def description(self, article):
        return "Latest comments to the article titled '%s'" % article.title

    def items(self, article):
        return Comment.objects.filter(object_pk=article.id, is_public=True,
                                      is_removed=False)[:10]

    def item_title(self, item):
        return item.user_name

    def item_link(self, item):
        article_url = reverse('article', args=(item.object_pk,))
        return "http://%s%s#c%d" % (self.site.domain, article_url, item.id)

    def item_description(self, item):
        return item.comment
