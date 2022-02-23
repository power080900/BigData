from django.urls import path
from . import views
urlpatterns = [
    path('todaysPlay',views.main),
]