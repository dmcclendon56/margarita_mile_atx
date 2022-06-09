from django.db import models

# Create your models here.

class Miles(models.Model):
    title = models.CharField(max_length=150)
    img = models.CharField(max_length=250)
        
    def __str__(self):
        return self.title  

    class Meta:
        ordering = ['title']
   

class Restaurant (models.Model):
    restaurant = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    margarita = models.CharField(max_length=500)
    price = models.IntegerField(default=0)  
    miles = models.ForeignKey(Miles, null = True, blank = True, on_delete=models.CASCADE, related_name="miles")
    
    def __str__(self):
        return self.restaurant

    class Meta:
        ordering = ['restaurant']


class Default(models.Model):
    title = models.CharField(max_length=150)
    img = models.CharField(max_length=250)
        
    def __str__(self):
        return self.title  

    class Meta:
        ordering = ['title']    

