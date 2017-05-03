from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^api/activity/$', views.ActivityList.as_view()),
    url(r'^api/activity/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),
    url(r'^api/timeEntry/$', views.TimeEntryList.as_view()),
    url(r'^api/timeEntry/(?P<pk>[0-9]+)/$', views.TimeEntryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
