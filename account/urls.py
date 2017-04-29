from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^userlist/$', views.userlist, name="userlist"),
  #  url(r'^adduser/$', views.adduser, name="adduser"),
  #  url(r'^userdetail/$', views.userdetail, name="userdetail"),
  #  url(r'^updateuser/$', views.updateuser, name="updateuser"),
  #  url(r'^deluser/$', views.deluser, name="deluser"),
  #  url(r'^userprofile/$', views.userprofile, name="userprofile"),
]