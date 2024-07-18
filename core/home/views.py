from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    people=[
        {"name":"albin","age":26},{"name":"albinqq","age":25},{"name":"albiqsqn","age":24},
        {"name":"albqsqsqin","age":23},{"name":"albqsqsin","age":22}
    ]
    
    return render(request,"index.html",context={'people':people})
def about(request):
    return render(request,'about.html')