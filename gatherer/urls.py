from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^API/', views.CreateView.as_view(), name='API'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
