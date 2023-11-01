from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),

    path('show/',views.showdata,name="showdata"),

    path('update/<id>',views.updatedata,name="updatedata"),
    path('delete/<id>',views.deletedata,name="deletedata"),
]