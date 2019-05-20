from django.shortcuts import render
from .models import RoleDistribution

# Create your views here.
def RoleManagement(request):
    context={'roles':RoleDistribution.objects.all()}
    return render(request,'RoleCreation/RoleManagement.html',context)
