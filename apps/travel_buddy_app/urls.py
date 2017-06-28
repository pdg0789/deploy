from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),

    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),

    url(r'^travels$', views.travels, name='travels'),
    url(r'^destination$', views.destination, name='destination'),
]
