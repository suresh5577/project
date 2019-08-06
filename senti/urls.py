from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_word', views.process_word, name='process'),
    url(r'^feature/', views.feature, name='features') 
]
