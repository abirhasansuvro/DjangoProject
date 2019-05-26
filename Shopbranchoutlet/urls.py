from django.urls import path
from . import views

urlpatterns = [
    path('',views.ShopBranchOutletView,name='ShopBranchOutletManagement'),
    path('create/' ,views.ShopBranchOutletCreate,name='ShopBranchOutletCreate'),
    path('create/sboinsert/' ,views.ShopBranchOutletInsert,name='ShopBranchOutletInsert'),
    path('view/<int:id>' ,views.ShopBranchOutletDetails,name='ShopBranchOutletDetails'),
]
