from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients, Cars
import re

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
        
        client = Clients.objects.filter(phone=phone)
        
        if client.exists():
            return render(request, 'clients.html', {'name': name, 'surname': surname, 'phone': phone, 'email': email, 'cars':zip(cars, regCar, year)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clients.html', {'name': name, 'surname': surname, 'phone': phone, 'cars':zip(cars, regCar, year)})
    
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