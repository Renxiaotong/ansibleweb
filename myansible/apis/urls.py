from django.contrib import admin
from django.urls import path ,include ,re_path
from apis import views

#后端api总控入口
urlpatterns = [
    re_path("^$",views.index,name="index"),
    re_path(r"^hostinfo/$",views.info,name="info"),
    re_path(r"^addhost/$",views.addhost,name="addhost"),
    re_path(r"^deletehost/$",views.deletehost,name="delete"),
    re_path(r"^deletetask/$",views.deletetask,name="deletetask"),
    re_path(r"^tasks/$",views.tasks,name="tasks"),
    re_path(r"^run/$",views.run,name="run"),
]
