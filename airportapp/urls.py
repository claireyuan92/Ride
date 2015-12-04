from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       #url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^$', index),
                       url(r'^logout/$', logout_page),
                       # If user is not login it will redirect to login page
                       url(r'^accounts/login/$',login),

                       #url(r'^accounts/weibologin/$',weibologin),



                           #'django.contrib.auth.views.login'),
                       url(r'^volunteer_register/$', volunteer_register),
                       url(r'^newstudent_register/$', newstudent_register),
                       url(r'^register/success/$', register_success),
                       url(r'^login_success/$', login_success),
                       url(r'^volunteer/$', volunteerView),
                       url(r'^newstudent/$', newstudentView),
                       url(r'^accounts/profile/$', login_success),
                       url(r'^submitPickup/$', submitPickup),
                      url(r'^upload/$', upload_pic),
                       )


