from django.shortcuts import render
from .models import blog
# Create your views here.
def blog1(request):
    post=blog.objects.all()
    return render (request,'blog/blog.html', {'post':post})

