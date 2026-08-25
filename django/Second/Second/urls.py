from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("listdisplay/", views.list1, name="listdisplay"),
    path("setdisplay/", views.set1, name="setdisplay"),
    path("dictdisplay/", views.dict1, name="dictdisplay"),
    path("tupledisplay/", views.tuple1, name="tupledisplay"),
    path("user1/", views.user1, name="user1"),
    path("user2/<int:id>/", views.user2, name="user2"),
]
