from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^members/', views.MembersPageView.as_view()),
    url(r'^labmembers/', views.LabMembersPageView.as_view()),
    url(r'^unreadcount/', views.UnreadIcon.as_view())
]