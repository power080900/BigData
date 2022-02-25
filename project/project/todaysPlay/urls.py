from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('todaysPlay',views.main),
    path('', views.main, name='main'),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('onlymember/', views.only_member, name="onlymember"),
]