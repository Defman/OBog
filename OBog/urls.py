from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from front import urls as front

admin.autodiscover()


urlpatterns = [
    url(r'^', include(front, namespace="front")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='auth_login'),
]
