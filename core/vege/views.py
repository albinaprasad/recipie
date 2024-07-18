from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def reciepes(request):
    if request.method == "POST":
        data=request.POST
        rimage=request.FILES.get("rimage")
        rname=data.get("rname")
        rdesc=data.get("rdesc")
        print(rname)
        print(rimage)
        receipe.objects.create(    
            rname=rname,
            rdesc=rdesc,
            rimage=rimage
            )
        
        
                              
    return render(request,"reciepes.html")

def show(request):
    queryset=receipe.objects.all()
    #search
    if request.GET.get("search_r"):
        queryset=queryset.filter(rname__icontains=request.GET.get("search_r"))
        
        
    context={'recipies':queryset}
    
    return render(request,"show.html",context)

def delete_recipie( request,id):
    queryset=receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/show.html/')

def update_items(request,id):
    queryset=receipe.objects.get(id=id)
    context={'recipies':queryset}
    if request.method =="POST":
        data=request.POST
        rimage=request.FILES.get("rimage")
        rname=data.get("rname")
        rdesc=data.get("rdesc")
        
        queryset.rname=rname
        queryset.rdesc=rdesc
        if rimage:
         queryset.rimage=rimage
        queryset.save()     
        return redirect('/show.html/')
    return render(request,"updates.html",context)
    