from django.db import models



# Create your models here.
class blog (models.Model):
    title=models.CharField(max_length=260)
    text=models.TextField()
    date=models.DateField() 
    time=models.TimeField()
    

    def __str__(self):
        return self.title 

    
