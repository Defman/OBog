from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index.as_view(), name="index"),
    url(r'^about$', about.as_view(), name="about"),
    url(r'^credits$', credits.as_view(), name="credits"),
    url(r'^contact$', ContactView.as_view(), name="contact"),
]