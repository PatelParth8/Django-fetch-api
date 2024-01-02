from django.urls import path
from . import views

urlpatterns = [
    path('',views.all,name="allpage"),
    path('sports',views.sports,name="sportspage"),
    path('fashion',views.fashion,name="fashionpage"),
    path('entertainment',views.entertainment,name="entertainmentpage"),
    path('technology',views.technology,name="technologypage")
]