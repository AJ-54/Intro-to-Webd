from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    #/music/
    url(r'^$',views.indexview.as_view(),name="index"),
    #/music/712/
    url(r'^(?P<pk>[0-9]+)/$' , views.detailview.as_view(), name='detail'),
    #/music/album/add/
    url(r'album/add/$',views.albumcreate.as_view(),name='album-add'),

]
