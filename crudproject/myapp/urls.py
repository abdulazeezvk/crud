from django.urls import path
from .import views

app_name='myapp'

urlpatterns = [
    path('index/',views.index,name="index"),

    path('show/',views.showdata,name="showdata"),

    path('update/<id>',views.updatedata,name="updatedata"),
    path('delete/<id>',views.deletedata,name="deletedata"),

    path('',views.account,name='account'),
]