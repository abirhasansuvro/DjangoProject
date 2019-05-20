from django.shortcuts import render
from .models import Tasks
from ModuleTask.models import Modules

# Create your views here.

def TaskManagement(request):
    context={'Tsks': Tasks.objects.all().order_by('order')}
    return render(request,'Task/TaskManagement.html',context)

def TaskCreate(request):
    context={'mdls': Modules.objects.all()}
    return render(request,'Task/TaskCreate.html',context)

def TaskView(request,id):
    try:
        T=Tasks.objects.get(pk=id)
    except T.DoesNotExist:
        raise Http404
    return render(request, 'Task/TaskView.html', {'Task': T})

def TaskEdit(request,id):
    try:
        T=Tasks.objects.get(pk=id)
    except T.DoesNotExist:
        raise Http404
    return render(request, 'Task/TaskEdit.html', {'Task': T})

def TaskUpdate(request):
    if(request.method=='POST'):
        OurRequest=request.POST
        T_id=Tasks.objects.get(code=OurRequest.get('element_code')).id
        Tasks.objects.get(id=T_id).delete()
        Task_list=OurRequest.getlist('element_task')
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
        T=Tasks(taskName=OurRequest.get('element_name'),code=OurRequest.get('element_code'),order=OurRequest.get('element_order'),
        moduleName=OurRequest.get('element_module'),view_task=view_T,add_task=add_T,
        save_task=save_T,edit_task=edit_T,delete_task=delete_T,
        print_task=print_T,cancel_task=cancel_T,reset_task=reset_T,
        find_task=find_T)
        T.save()

    context={'Tsks': Tasks.objects.all().order_by('order')}
    return render(request,'Task/TaskManagement.html',context)
