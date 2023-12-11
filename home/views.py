from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

#This function renders the home.html file when called.
def home(request): #The request argument is created whenever a page loads, it contains metadata
    messages.info(request,"Welcome to home page")
    return render(request,"home/home.html", {})

from .models import *
def index(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            table = CarDb()
            table.maker = request.POST.get('maker')
            table.genmodel = request.POST.get('genmodel')
            table.genmodel_id = request.POST.get('genmodel_id')
            table.adv_id = request.POST.get('adv_id')
            table.adv_year = request.POST.get('adv_year')
            table.adv_month = request.POST.get('adv_month')
            table.colour = request.POST.get('colour')
            table.reg_year = request.POST.get('reg_year')
            table.bodytype = request.POST.get('bodytype')
            table.mileage = request.POST.get('mileage')
            table.engine_size = request.POST.get('engine_size')
            table.gearbox = request.POST.get('gearbox')
            table.fuel_type = request.POST.get('fuel_type')
            table.price = request.POST.get('price')
            table.seat_num = request.POST.get('seat_num')
            table.door_num = request.POST.get('door_num')
            table.save()
            messages.success(request,"Record saved successfully")
        return redirect('carlist')
    return render(request,'home/home.html')