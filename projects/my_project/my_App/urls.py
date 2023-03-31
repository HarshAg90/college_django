from django.urls import path
from .views import homepageView,second_View

urlpatterns =[
    path("",homepageView, name="homo"),
    path("page_2",second_View, name="uwu"),
]