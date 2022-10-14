
from django.urls import path
from hp import views 

urlpatterns = [
    
    path('add/',views.shirt),
    path('new/',views.pant),
]
