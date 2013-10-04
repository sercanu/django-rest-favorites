from django.conf.urls import patterns, url
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

from core import views


# API endpoints
urlpatterns = format_suffix_patterns(patterns('core.views',
    url(r'^api/$', 'api_root'),
    url(r'^favorites/$', views.FavoriteList.as_view(), name='favorite-list'),
    url(r'^favorites/(?P<pk>[0-9]+)/$', views.FavoriteDetail.as_view(), name='favorite-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>)/$', views.UserDetail.as_view(), name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)