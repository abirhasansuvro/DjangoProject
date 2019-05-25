from django.shortcuts import render,redirect
from .models import RoleDistribution,Roles
from ModuleTask.models import Modules
from Task.models import Tasks

# Create your views here.
def RoleManagement(request):
    context={'roles':Roles.objects.all()}
    return render(request,'RoleCreation/RoleManagement.html',context)

def RoleCreate(request):
    context={'mdls':Modules.objects.all(),'tsks':Tasks.objects.all()}
    return render(request,'RoleCreation/RoleCreate.html',context)


def RoleInsert(request):
    if request.method=='POST':
        OurRequest=request.POST
        R=Roles(name=OurRequest.get('role_name'))
        R.save()

        tasks=Tasks.objects.all()
        for t in tasks:
            Task_list=OurRequest.getlist(t.taskName+'_element_task')
            if 'view_checked' in Task_list:
                view_T=1
            else:
                view_T=0

            if 'add_checked' in Task_list:
                add_T=1
            else:
                add_T=0

            if 'save_checked' in Task_list:
                save_T=1
            else:
                save_T=0

            if 'edit_checked' in Task_list:
                edit_T=1
            else:
                edit_T=0

            if 'delete_checked' in Task_list:
                delete_T=1
            else:
                delete_T=0

            if 'print_checked' in Task_list:
                print_T=1
            else:
                print_T=0

            if 'cancel_checked' in Task_list:
                cancel_T=1
            else:
                cancel_T=0

            if 'reset_checked' in Task_list:
                reset_T=1
            else:
                reset_T=0

            if 'find_checked' in Task_list:
                find_T=1
            else:
                find_T=0
            RoleD=RoleDistribution(Role=R,Task=t,view_task=view_T,add_task=add_T,save_task=save_T,edit_task=edit_T,
            delete_task=delete_T,print_task=print_T,cancel_task=cancel_T,reset_task=reset_T,find_task=find_T)
            RoleD.save()
    context={'roles':Roles.objects.all()}
    return redirect('/RoleCreation/')

def RoleView(request,id):
    Role_=Roles.objects.get(id=id)
    context={'detailRoles':RoleDistribution.objects.filter(Role=Role_),
    'mdls':Modules.objects.all(),'tsks':Tasks.objects.all(),'R':Role_}
    return render(request,'RoleCreation/RoleView.html',context)

def RoleEdit(request,id):
    Role_=Roles.objects.get(id=id)
    context={'detailRoles':RoleDistribution.objects.filter(Role=Role_),
    'mdls':Modules.objects.all(),'tsks':Tasks.objects.all(),'R':Role_}
    return render(request,'RoleCreation/RoleEdit.html',context)

def RoleUpdate(request):
    if request.method=='POST':
        OurRequest=request.POST
        R=Roles.objects.get(name=OurRequest.get('role_name'))
        RoleDistribution.objects.filter(Role=R).delete()
        tasks=Tasks.objects.all()
        for t in tasks:
            Task_list=OurRequest.getlist(t.taskName+'_element_task')
            if 'view_checked' in Task_list:
                view_T=1
            else:
                view_T=0

            if 'add_checked' in Task_list:
                add_T=1
            else:
                add_T=0

            if 'save_checked' in Task_list:
                save_T=1
            else:
                save_T=0

            if 'edit_checked' in Task_list:
                edit_T=1
            else:
                edit_T=0

            if 'delete_checked' in Task_list:
                delete_T=1
            else:
                delete_T=0

            if 'print_checked' in Task_list:
                print_T=1
            else:
                print_T=0

            if 'cancel_checked' in Task_list:
                cancel_T=1
            else:
                cancel_T=0

            if 'reset_checked' in Task_list:
                reset_T=1
            else:
                reset_T=0

            if 'find_checked' in Task_list:
                find_T=1
            else:
                find_T=0
            RoleD=RoleDistribution(Role=R,Task=t,view_task=view_T,add_task=add_T,save_task=save_T,edit_task=edit_T,
            delete_task=delete_T,print_task=print_T,cancel_task=cancel_T,reset_task=reset_T,find_task=find_T)
            RoleD.save()
    context={'roles':Roles.objects.all()}
    return redirect('/RoleCreation/')
