from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^userlist/$', views.userlist, name="userlist"),
    url(r'^adduser/$', views.adduser, name="adduser"),
    url(r'^saveuser/$', views.saveuser, name="saveuser"),
    url(r'^userdetail/id=(?P<user_id>[0-9]+)/$', views.userdetail, name="userdetail"),
    url(r'^updateuser/id=(?P<user_id>[0-9]+)/$', views.updateuser, name="updateuser"),
    url(r'^saveupdateuser/id=(?P<user_id>[0-9]+)/$', views.saveupdateuser, name="saveupdateuser"),
    url(r'^deluser/id=(?P<user_id>[0-9]+)/$', views.deluser, name="deluser"),
    url(r'^userprofile/id=(?P<user_id>[0-9]+)/$', views.userprofile, name="userprofile"),
]
