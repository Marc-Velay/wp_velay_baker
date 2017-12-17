
# Paths within the api

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api.views import *

urlpatterns = {
    #Authentication urls
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/', CustomObtainAuthToken.as_view()),
    url(r'^', CustomObtainAuthToken.as_view()),

    #User-related urls
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/add/$', UserAddView.as_view(), name="add_users"),
    url(r'^users/update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name="update_users"),
    url(r'^users/delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(), name="delete_users"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),

    #Portfolio related urls
    url(r'^portfolio/',include([
        url(r'^add/$', CreatePortfolioView.as_view(), name="add_portfolio"),
        url(r'^update/(?P<pk>[0-9]+)/$', UpdatePortfolioView.as_view(), name="update_portfolio"),
        url(r'^delete/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name="delete_portfolio"),
        url(r'^list/$', PortfolioList.as_view(), name="list_portfolio"),
        url(r'^item/(?P<pk>[0-9]+)/$', GetItemsFromPortfolio.as_view(), name="get_item_portfolio"),
        url(r'^item/link/(?P<pk>[0-9]+)/$', LinkItemToPortfolio.as_view(), name="link_portfolio"),
        url(r'^item/remove/(?P<pk>[0-9]+)/$', RemoveItemFromPortfolio.as_view(), name="remove_item_portfolio"),
        url(r'^get/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name="get_portfolio"),
    ])),

    #Item management urls
    url(r'^items/$', CreateView.as_view(), name="create_item"),
    url(r'^items/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="get_item"),
    url(r'^(?P<item>\w+)/',include([
        url(r'^(?P<year>[0-9]{4})/$', item_year.as_view(), name="year"),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', item_day.as_view(), name="day"),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', item_month.as_view(), name="month"),
        url(r'^last24/$', item_last24.as_view(), name="Last 24 hours"),
    ])),

}

urlpatterns = format_suffix_patterns(urlpatterns)
