from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aykhan", views.aykhan, name="aykhan"),
    path("<int:a>+<int:b>", views.adder, name="adder"),
    path("<str:name>", views.greet, name="greet")
    
]