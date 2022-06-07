from django.db import models

# Create your models here.

class Miles(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title  

class restaurant (models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    margarita = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Miles, on_delete=models.CASCADE, related_name="restaurant")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


      

