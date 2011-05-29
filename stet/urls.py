from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from stet.models import Article

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        model=Article,
    ), name='list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Article,
    ), name='article'),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
