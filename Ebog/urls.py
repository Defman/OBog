from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^list/(?:page-(?P<page>\d+)/)?$', BookView.List.as_view(), name="list"),
    url(r'^create/$', BookView.Create.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)', BookView.Detail.as_view()),
    url(r'^section/create$', SectionView.Create.as_view(), name="create_section"),
    url(r'^section/page/create/$', PageView.Create.as_view(), name="create_page"),
]
