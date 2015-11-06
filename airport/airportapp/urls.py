from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       #url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^$', index),
                       url(r'^logout/$', logout_page),
                       # If user is not login it will redirect to login page
                       url(r'^accounts/login/$',
                           'django.contrib.auth.views.login'),
                       url(r'^volunteer_register/$', volunteer_register),
                       url(r'^newstudent_register/$', newstudent_register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', home),
                       )
