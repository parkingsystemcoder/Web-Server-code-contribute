#server system info

from django.conf.urls import url
from . import views

urlpatterns = [

    #/serverSystemInfo/
    url(r'^$', views.index, name='index'),

    #/serverSystemInfo/<userID>
    url(r'^(?P<userID>[0-9]+)/$', views.main, name='userServerSystemInfo'),
]
