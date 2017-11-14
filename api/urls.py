
# Paths within the api

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CreateView, DetailsView, item_year, item_day, item_month

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^items/$', CreateView.as_view(), name="create"),
    url(r'^(?P<item>\w+)/',include([
        url(r'^(?P<year>[0-9]{4})/$', item_year.as_view(), name="year"),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', item_day.as_view(), name="day"),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', item_month.as_view(), name="month"),
    ])),
}

urlpatterns = format_suffix_patterns(urlpatterns)
