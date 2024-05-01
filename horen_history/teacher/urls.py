from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("parents/", views.parent, name='parents'),
    path("students/", views.student, name='students'),
    path("methodically/", views.methodically, name="methodically"),
    path("info/", views.info, name="info")
]