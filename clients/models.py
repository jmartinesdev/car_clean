from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
class Cars(models.Model):
    car = models.CharField(max_length=20)
    regCar = models.CharField(max_length=8)
    year = models.IntegerField()
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.car