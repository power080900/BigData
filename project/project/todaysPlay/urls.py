from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('googlemap/', views.map),
    path('main/', views.main),
    path('randomslot/', views.randomslot),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signInPage/', views.signInPage, name='signInPage'),
    path('location1/', views.location1, name='location1'),
    path('location2/', views.location2, name='location2'),
    path('info/', views.info),
]