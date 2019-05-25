from django.urls import path
from . import views

urlpatterns = [
    path('',views.RoleAssignment,name='RoleAssignment'),
    path('RoleAssign/',views.NewRoleAssign,name='NewRoleAssign'),
    path('RoleAssign/RoleInsert/',views.UserInsert,name='UserInsert'),
    # path('RoleCreate/RoleInsert/',views.RoleInsert,name='RoleInsert'),
    # path('RoleForTask/',views.RoleForTask,name='RoleForTask'),
]
