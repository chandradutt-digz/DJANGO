from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('allemp/', views.allemp),
    path('addemp/', views.addemp, name='addemp'),
    path('addemp/<int:id>/', views.addemp, name='addemp'),
    path('removeemp/', views.removeemp, name='removeemp'),
    path('removeemp/<int:emp_id>', views.removeemp, name='removeemp'),
    path('filteremp/', views.filteremp, name='filteremp'),
    path('updateemp/<int:id>/', views.updateemp, name='updateemp'),
    path('editemp/<int:id>/', views.editemp, name='editemp'),
]
