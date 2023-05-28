from django.shortcuts import render
from .forms import ImageForm
from .models import Image



# Create your views here.
def homeapp(request):
    if request.method == "POST": #this to allow the user to upload
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'app/homeapp.html',{'img':img, 'form':form})

