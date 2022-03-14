from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('loginPage/', views.loginPage, name='loginPage'),
    path('googlemap/', views.map),
    path('main/', views.main, name='main'),
    path('randomslot/', views.randomslot),
    path('signInPage/', views.signInPage, name='signInPage'),
    path('location/', views.location, name='location'),
    path('logout/', views.logout, name="logout"),
    path('info1/', views.info1, name="info1"),
    path('info2/', views.info1, name="info2"),
]