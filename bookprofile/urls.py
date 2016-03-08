from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^profile$', profile.as_view(), name="profile"),
    url(r'^mybooks|minebøger$', mybooks.as_view(), name="mybooks"),
]