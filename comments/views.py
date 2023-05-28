from django.shortcuts import render
from .models import Comments

# Create your views here.
def comments(request):
 if request.method == 'POST':
   #1: get the data from the form
   v_name = request.POST.get('name')
   v_massage = request.POST.get('message')
   #2: send this data to the DB(Models)
   v_home = Comments(name=v_name,massage=v_massage)
   v_home.save()
   comment=Comments.objects.all()
   return  render(request,'comments/comments.html', {'comment':comment})
 else:
   comment=Comments.objects.all()
   return  render(request,'comments/comments.html', {'comment':comment})