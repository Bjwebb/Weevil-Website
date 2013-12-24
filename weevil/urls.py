from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.php$', 'weevil.legacy.redirect'),
)

urlpatterns += patterns('weevil.views',
    url(r'^$', 'home', name='home'),
    url(r'^issue(\d+)$', 'magazine', name='magazine'),
    url(r'^issue(\d+)/([-\w\d]+)$', 'article', name='article'),
    url(r'^contributors$', 'contributors', name='contributors'),
    url(r'^contributors/(writers|illustrators)$', 'contributors', name='contributors'),
    url(r'^contributors/([-\w\d]+)$', 'contributor', name='contributor'),
    url(r'^news$', 'news', name='news'),
    #url(r'^news/([-\w\d]+)$', 'news_article', name='news_article'),
    url(r'^committee/([\d]+)$', 'committee', name='committee'),
    # TMP
    url('^committee/$', RedirectView.as_view(url='/committee/2013', permanent=False)),
    url('^committee/previous', RedirectView.as_view(url='/committee/2011', permanent=False)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url('^(.*/)$', 'flatpage', name='flatpage'),
)
