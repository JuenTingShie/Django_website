from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50,blank=True)
    spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name