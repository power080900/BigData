from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('todaysPlay',views.main),
    # path('choosePage/',views.choosePage(), name='choosePage'),
]