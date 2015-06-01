from django.conf.urls import patterns, url
from apps.user_logs import views

urlpatterns = patterns('',
                       url(r'^$', views.user_logs, name='login'),
                       url(r'^timein/$', views.record_timein,
                           name='timein'),
                       url(r'^timeout/$', views.record_timeout,
                           name='timeout'),
                       )
