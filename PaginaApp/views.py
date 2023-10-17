from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request,"PaginaApp/index.html")


def service(request):
    
    return render(request,"PaginaApp/service.html")

def contact(request):
    
    return render(request,"PaginaApp/contact.html")


def about(request):
    
    return render(request,"PaginaApp/about.html")


def pages(request):
    
    return render(request,"PaginaAPP/pages.html")

def blog(request):
    
    return render(request,"PaginaAPP/blog.html")

def detail(request):
    
    return render(request,"PaginaAPP/detail.html")

def price(request):
    
    return render(request,"PaginaApp/price.html")


def feature(request):
    
    return render(request,"PaginaApp/feature.html")


def team(request):
    
    return render(request,"PaginaApp/team.html")

def testimonial(request):
    
    return render(request,"PaginaAPP/testimonial.html")

def quote(request):
    
    return render(request,"PaginaApp/quote.html")








