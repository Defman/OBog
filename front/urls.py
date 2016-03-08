from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index.as_view(), name="index"),
    url(r'^om|about$', about.as_view(), name="about"),
    url(r'^taktil|credits$', credits.as_view(), name="credits"),

]