from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"base.html")
def Menu(request):
    return render(request,"menu.html")
def About(request):
    return render(request,"about.html")
def Book(request):
    return render(request,"contact.html")
