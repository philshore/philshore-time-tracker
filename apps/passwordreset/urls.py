from django.conf.urls import patterns, url
from apps.passwordreset import views

urlpatterns = patterns('',
                       url(r'^password_reset/$',
                           views.password_reset,
                           name = 'password reset' )
                       )
