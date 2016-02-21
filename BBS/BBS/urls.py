from django.conf.urls import patterns, include, url
from app import urls
#import app.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS.views.home', name='home'),
    # url(r'^BBS/', include('BBS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bbs/', include('app.urls')),
    #url(r'^bbs/', include(app.urls)),
)
