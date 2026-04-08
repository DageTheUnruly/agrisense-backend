from django.urls import path
from . import views

urlpatterns = [
    # Ensure it says views.get_sensors
    path('sensors/', views.get_sensors, name='get_sensors'),
    path('login/', views.login_user, name='login'),
]