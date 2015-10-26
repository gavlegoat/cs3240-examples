from django.conf.urls import url, patterns
from . import views

urlpatterns =  [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload_file, name='upload'),
    url(r'^success$', views.success, name='success')
]
