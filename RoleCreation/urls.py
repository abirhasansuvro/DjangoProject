from django.urls import path
from . import views

urlpatterns = [
    path('',views.RoleManagement,name='RoleManagement'),
    path('RoleView/<int:id>',views.RoleView,name='RoleView'),
    path('RoleEdit/<int:id>',views.RoleEdit,name='RoleEdit'),
    path('RoleEdit/RoleUpdate/',views.RoleUpdate,name='RoleUpdate'),
    path('RoleCreate/',views.RoleCreate,name='RoleCreate'),
    path('RoleCreate/RoleInsert/',views.RoleInsert,name='RoleInsert'),
]
