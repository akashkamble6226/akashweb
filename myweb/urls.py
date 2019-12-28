from django.urls import path

from . import views


urlpatterns=[

    path('',views.home, name='home'),
    path('proj',views.proj, name='proj'),
    path('pics',views.pics, name='pics'),

    path('home',views.home2, name='home2'),
]