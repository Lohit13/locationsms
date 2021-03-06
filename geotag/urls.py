from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geotag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'geotag.views.index', name='home'),
    url(r'^msg/(?P<tag>.+)/$', 'geotag.views.msg', name='msg'),

)
