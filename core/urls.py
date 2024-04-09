from django.urls import path 
from .views import *

urlpatterns = [
    path("",recipes,name="recipes"),
    path("delete_recipe/<int:id>",delete_recipe,name="delete"),
    path("update/<int:id>",update_recipe,name="update"),
]


