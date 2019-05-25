from django.shortcuts import render,redirect
from RoleCreation.models import Roles
from .models import UserWithRole

def RoleAssignment(request):
    context={'roles':UserWithRole.objects.all()}
    return render(request, 'RoleAssignment/RoleAssignment.html', context);


def NewRoleAssign(request):
    context={'roles':Roles.objects.all()}
    return render(request, 'RoleAssignment/NewRoleAssign.html', context)

def UserInsert(request):
    if request.method=='POST':
        OurRequest=request.POST
        u_name=OurRequest.get('userName')
        p_word=OurRequest.get('password')
        email=OurRequest.get('useremail')
        display_name=OurRequest.get('displayName')
        image=OurRequest.get('userimage')
        mobile_no=OurRequest.get('mobileno')
        role_list=OurRequest.getlist('roleselect')
        U=UserWithRole(UserName=u_name,DisplayName=display_name,ProfilePic=image,email=email,password=p_word,Mobile=mobile_no)
        U.save()
        for role in role_list:
            R=Roles.objects.filter(name=role).first()
            U.role.add(R)
    return redirect('/RoleAssignment/')
