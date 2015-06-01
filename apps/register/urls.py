from django.conf.urls import patterns, url
from apps.register import views

urlpatterns = patterns('',
                       url(r'^$', views.register, name='register'),
                       url(r'^success/$', views.success_register,
                           name='register_success')
                       )
