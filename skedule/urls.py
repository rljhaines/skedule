from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.views import greeting

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skedule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^website/', include(website.urls)),
)
