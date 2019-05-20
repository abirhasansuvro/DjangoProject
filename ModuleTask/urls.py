from django.urls import path
from . import views

urlpatterns = [
    path('',views.ModuleManagement,name='ModuleManagement'),
    path('View/<int:id>',views.ModuleView,name='ModuleView'),
    path('Edit/<int:id>',views.ModuleEdit,name='ModuleEdit'),
    path('ModuleCreate/',views.ModuleCreate,name='ModuleCreate'),
    path('ModuleCreate/ModuleInsert/',views.ModuleInsert,name='ModuleInsert'),
    path('Edit/ModuleUpdate/',views.ModuleUpdate,name='ModuleUpdate'),
]
