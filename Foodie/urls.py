from django.conf.urls import patterns, url
from Foodie import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^upload/', views.upload, name= 'upload'),
        url(r'^about/', views.about, name= 'about'),
        url(r'^location/', views.location, name= 'location'),
        url(r'^special/', views.special, name= 'special'),
        url(r'^privacy/', views.privacy, name= 'privacy'),
        url(r'^contact/', views.contact, name= 'contact'),
        url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='category'),
        #url(r'^upload_csv', views.upload, name = 'upload'),
        )