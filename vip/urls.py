from django.conf.urls import url

from vip import views

urlpatterns = [
    url(r'/', views.index, name='index'),
]
