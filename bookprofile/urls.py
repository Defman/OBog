from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^profile$', Profile.as_view(), name="profile"),
    url(r'^mybooks|minebøger$', Mybooks.as_view(), name="mybooks"),
]