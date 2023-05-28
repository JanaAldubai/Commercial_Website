from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'page/home.html')

def about(request):
    return render(request,'page/about.html')

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        Subject=request.POST.get('Subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,Subject=Subject,message=message)
        contact.save()
        return render(request,'page/respons.html')
    
    return render(request,'page/contact.html')

