from django.urls import path
from . import views

urlpatterns = [
    path('',views.TaskManagement,name='TaskManagement'),
    path('Create/',views.TaskCreate,name='TaskCreate'),
    path('Create/TaskInsert/',views.TaskInsert,name='TaskInsert'),
    path('Edit/<int:id>',views.TaskEdit,name='TaskEdit'),
    path('View/<int:id>',views.TaskView,name='TaskView'),
    path('Edit/TaskUpdate/',views.TaskUpdate,name='TaskUpdate'),
]
