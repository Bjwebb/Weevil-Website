from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('weevil.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^weevil/', include('weevil.foo.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url('^(.*/)$', 'flatpage', name='flatpage'),
)
