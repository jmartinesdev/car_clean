from django.shortcuts import render
from django.http import HttpResponse

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
        

        
        print(name)
        print(cars)
        print(regCar)
        print(year)
        
        return HttpResponse('teste')