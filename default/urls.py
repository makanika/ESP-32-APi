from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.homeView, name='homeView' ),
    path('servo', view=views.servo, name='servoView' ),
]