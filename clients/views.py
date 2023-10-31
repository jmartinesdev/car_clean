from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients, Cars

# Create your views here.
def clients(request):
    if request.method == "GET":
        return render(request, 'clients.html')
    elif request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        cars = request.POST.getlist('car')
        regCar = request.POST.getlist('reg-car')
        year = request.POST.getlist('year')
    
        client = Clients(
            name = name,
            surname = surname,
            email = email,
            phone = phone
        )
        
        client.save()
        
        for car, r_car, y in zip(cars, regCar, year):
            car_models = Cars(car=car, regCar=r_car, year=int(y), clients=client)
            car_models.save()
            
        
        return HttpResponse('teste')