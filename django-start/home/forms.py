from django.forms import ModelForm
from .models import Customer,Adress

# Create the form class.
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        


class AdressForm(ModelForm):
    class Meta:
        model = Adress
        fields = '__all__'
        
