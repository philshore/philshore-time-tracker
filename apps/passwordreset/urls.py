from django.conf.urls import patterns, url
from apps.passwordreset import views

urlpatterns = patterns('',
                       url(r'^password_reset/$',
                           views.password_reset,
                           name = 'password reset' ),
                       url(r'^change_password/$',
                           views.change_password,
                           name = 'password reset' ),
                       )
