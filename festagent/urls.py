from django.conf.urls import patterns, include, url
from catalog import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'festagent.views.home', name='home'),
    # url(r'^festagent/', include('festagent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list')
)
