from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('todaysPlay/',views.main),
    path('googlemap/', views.map),
    path('main/', views.main),
    path('randomslot/', views.randomslot),
]