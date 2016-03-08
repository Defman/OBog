from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from front import urls as front
from Ebog import urls as ebook
from store import urls as store
from bookprofile import urls as profile

admin.autodiscover()


urlpatterns = [
    url(r'^', include(front, namespace="front")),
    url(r'^book/', include(ebook, namespace="ebook")),
    url(r'^store/', include(store, namespace="store")),
    url(r'^user/', include(profile, namespace="user")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='auth_login'),
]

