from django.shortcuts import render
from .forms import CustomerForm,AdressForm
from django.http import HttpResponse
from .models import Room
def home(request):
    Rooms = Room.objects.all()
    context = {'Rooms':Rooms}
    return render(request,'home/index.html',context)

def rezervasyon(request):
    data=request.data.get('adsoyad')
    print(data)
    return HttpResponse('Başarılı')

def room_detail(request,roomnum):
    if request.method == 'POST': # If the form has been submitted...
        customerform = CustomerForm(request.POST) # A form bound to the POST data
        adressform = AdressForm(request.POST)
        print(musteriform)
        print(adresform)
        if customerform.is_valid() and adressform.is_valid(): # All validation rules pass
            print("Valid worked")
            customerform.save()
            adressform.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        customerform = CustomerForm() # A form bound to the POST data
        adressform = AdressForm()
    return render(request,'home/roomdetail.html',{'customerform': customerform,'adressform':adressform})


# def rezervasyon(request):
#      # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
        
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()


def about(request):
    return render(request,'home/about.html')