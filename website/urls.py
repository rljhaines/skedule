from django.conf.urls import patterns, include, url
from website import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skedule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.greeting),
)
