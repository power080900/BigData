from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('loginPage/', views.loginPage, name='loginPage'),
    path('googlemap/', views.map),
    path('main/', views.main, name='main'),
    path('randomslot/', views.randomslot),
    path('signInPage/', views.signInPage, name='signInPage'),
    path('logout/', views.logout, name="logout"),
    path('info1/', views.info1, name="info1"),
    path('info2/', views.info2, name="info2"),
    path('location1/', views.location1, name='location1'),
    path('location2/', views.location2, name='location2'),
]