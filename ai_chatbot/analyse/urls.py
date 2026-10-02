from django.urls import path
from .views import*

urlpatterns = [
    path('analyse/',analyseAPI.as_view()),
   
]