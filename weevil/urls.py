from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('weevil.views',
    url(r'^$', 'home', name='home'),
    url(r'^issue(\d+)$', 'magazine', name='magazine'),
    url(r'^issue(\d+)/([-\w\d]+)$', 'article', name='article'),
    url(r'^contributor/([-\w\d]+)$', 'contributor', name='contributor'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url('^(.*/)$', 'flatpage', name='flatpage'),
)
