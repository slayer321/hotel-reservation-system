from django.shortcuts import render,redirect
from .forms import CustomerForm,AdressForm
from django.http import HttpResponse
from .models import *

def home(request):
    Rooms = Room.objects.all()
    context = {'Rooms':Rooms}
    return render(request,'home/index.html',context)

def reservation(request):
    if request.method == 'POST':
        # customer
        customer_name = request.POST['customer_name']
        customer_last_name = request.POST['customer_last_name']
        identity_number = request.POST['identity_number']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        # adress
        country = request.POST['country']
        city = request.POST['city']
        neighborhood = request.POST['neighborhood']
        street = request.POST['street']
        post_code = request.POST['post_code']
        apt_number = request.POST['apt_number']
        door_number = request.POST['door_number']
        # Bill
        entry_date =request.POST['entry_date']
        exit_date =request.POST['exit_date']
        # data save
        adressdata = Adress.objects.create(country=country,city=city,postcode=post_code,neighboorhood=neighborhood,street=street,aptNumber=apt_number,doorNumber=door_number)
        customer = Customer.objects.create(customerName=customer_name,customerLastName=customer_last_name,customerIdentityNumber=identity_number,customerPhoneNumber=phone_number,customerBirthDate=birth_date,adress=adressdata)
        # model objects
        return redirect('home:reservation')
    else:
        return redirect('home:home1')

def room_detail(request,roomnum):
    odabilgim = Room.objects.filter(roomNumber=roomnum)
    return render(request,'home/roomdetail.html',{'odabilgim': odabilgim})


def about(request):
    return render(request,'home/about.html')