from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^list/(?:page-(?P<page>\d+)/)?$', Book.List.as_view(), name="list"),
    url(r'^create/$', Book.Create.as_view(), name="create"),
    url(r'^section/create$', Section.Create.as_view(), name="create_section"),
    url(r'^section/page/create/$', Page.Create.as_view(), name="create_page"),
]
