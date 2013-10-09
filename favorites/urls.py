from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.conf.urls import patterns, url, include
from rest_framework import routers
from core import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'favorites.views.home', name='home'),
    # url(r'^favorites/', include('favorites.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls')),

)
