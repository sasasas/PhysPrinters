from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from webproject2 import views 

urlpatterns = patterns('',
    # Example:
    # (r'^web_project/', include('web_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	('^home/$', views.home),
	('^printers/$', views.printers),
	('^printers/searchcomputer/$', views.searchcomputer),
	('^printers/searchcomputer/submitrequest/$', views.submitrequest),
	('^confirmation/$', views.confirmation)
)
