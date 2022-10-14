
from django.urls import path
from apple import views 

urlpatterns = [
    
    path('cal/',views.calm ),
    path('qui/', views.quit),
    
]
