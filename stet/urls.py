from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from stet.models import Article

urlpatterns = patterns('',
    (r'^$', ListView.as_view(
        model=Article,
    )),
    (r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Article,
    )),
    (r'^comments/', include('django.contrib.comments.urls')),
)
