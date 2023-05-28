from django.db import models

# Create your models here.

class Comments(models.Model):
    name = models.CharField(max_length=150)
    massage = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name