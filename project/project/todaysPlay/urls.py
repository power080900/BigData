from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('googlemap/', views.map),
    path('main/', views.main),
    path('randomslot/', views.randomslot),
    path('loginPage/', views.loginPage),
    path('signInPage/', views.signInPage),
    path('location/', views.location, name='location'),
    path('info/', views.info),
]