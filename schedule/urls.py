from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from schedule import views

urlpatterns = patterns('',
     url(r'^add/$', views.addMeeting.as_view(), name="add"),
     url(r'all/$', views.allMeetings.as_view(), name="all"),
)