from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # Products=Product.objects.all()
    # n=len(Products)
    # nSlides=n//4+ceil(n/4-n//4)
    # allprod=[[Products,range(1,nSlides),nSlides],[Products,range(1,nSlides),nSlides]]
    # param={'product':Products,'no_of_slides':nSlides,'range':range(1,nSlides)}
    allprod=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides=n//4+ceil(n/4-n//4)
        allprod.append([prod,range(1,nSlides),nSlides])
    param={'allProds':allprod}
    return render(request,'shop/index.html',param)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
