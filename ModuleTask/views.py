from django.shortcuts import render
from .models import Modules

# Create your views here.
def ModuleManagement(request):
    context={'mdls': Modules.objects.all().order_by('order')}
    return render(request,'ModuleTask/ModuleManagement.html',context)


def ModuleView(request,id):
    try:
        M=Modules.objects.get(pk=id)
    except M.DoesNotExist:
        raise Http404
    return render(request, 'ModuleTask/ModuleView.html', {'Module': M})


def ModuleEdit(request,id):
    try:
        M=Modules.objects.get(pk=id)
    except M.DoesNotExist:
        raise Http404
    return render(request, 'ModuleTask/ModuleEdit.html', {'Module': M})

def ModuleUpdate(request):
    if(request.method=='POST'):
        OurRequest=request.POST
        M_id=Modules.objects.get(code=OurRequest.get('element_code')).id
        Modules.objects.get(id=M_id).delete()
        M=Modules(name=OurRequest.get('element_name'),code=OurRequest.get('element_code'),order=OurRequest.get('element_order'))
        M.save()

    context={'mdls': Modules.objects.all().order_by('order')}
    return render(request,'ModuleTask/ModuleManagement.html',context)

def ModuleCreate(request):
    return(request,'ModuleTask/ModuleCreate.html',{})

def ModuleInsert(request):
    if(request.method=='POST'):
        OurRequest=request.POST
        code='MDL_'+Modules.objects.all().count
        M=Modules(name=OurRequest.get('element_name'),code=OurRequest.get('element_code'),order=OurRequest.get('element_order'))
        M.save()

    context={'mdls': Modules.objects.all().order_by('order')}
    return render(request,'ModuleTask/ModuleManagement.html',context)
