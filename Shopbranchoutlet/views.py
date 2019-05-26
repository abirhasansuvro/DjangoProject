from django.shortcuts import render, redirect
from .models import SBO

def ShopBranchOutletView(request):
    context={
        'sbos': SBO.objects.all()
    }
    return render(request, 'Shopbranchoutlet/ShopBranchOutletTemplate.html', context)


def ShopBranchOutletCreate(request):
    return render(request, 'Shopbranchoutlet/ShopBranchOutletCreate.html', {})


def ShopBranchOutletInsert(request):
    if request.method == 'POST':
        r = request.POST
        nam = r.get('sboName')
        loc = r.get('sboLocation')
        noe = r.get('sboNoOfEmployee')
        are = r.get('sboArea')
        type_list = r.getlist('typeselect')
        b_s = 0
        s_s = 0
        o_s = 0
        if 'b' in type_list:
            b_s = 1
        if 's' in type_list:
            s_s = 1
        if 'o' in type_list:
            o_s = 1
        sbo = SBO(name=nam, location=loc, no_of_employees=noe, area_square_ft=are, is_shop=s_s, is_branch=b_s, is_outlet=o_s)
        sbo.save()
    return redirect('/shopbranchoutlet/')

def ShopBranchOutletDetails(request, id):
    context = {
        'sbo' : SBO.objects.get(id=id)
    }
    return render(request, 'Shopbranchoutlet/ShopBranchOutletDetails.html', context)
