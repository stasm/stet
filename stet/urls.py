from django.conf.urls.defaults import *
from django.views.generic import ArchiveIndexView, DetailView

from stet.models import Article
from stet.feeds import ArticleFeed, CommentsForArticleFeed

urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view(
        model=Article,
        date_field='pub_date',
        paginate_by=2,
        template_name='stet/article_home.html'
    ), name='index'),
    url(r'^p/(?P<page>[0-9]+)$', ArchiveIndexView.as_view(
        model=Article,
        date_field='pub_date',
        paginate_by=2
    ), name='list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Article,
    ), name='article'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)$', DetailView.as_view(
        model=Article,
    ), name='article_with_slug'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^feed$', ArticleFeed()),
    (r'^feed/(?P<article_id>\d+)$', CommentsForArticleFeed()),
)
