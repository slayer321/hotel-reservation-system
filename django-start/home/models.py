from django.db import models
from datetime import date

class Adress(models.Model):
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    postcode = models.CharField(max_length=50)
    neighboorhood = models.CharField(max_length=15)
    street = models.CharField(max_length=50)
    aptNumber = models.CharField(max_length=50)
    doorNumber = models.CharField(max_length=50)
    def __str__(self):
        return self.country

class Customer(models.Model):  
    customerName= models.CharField(max_length=50)
    customerLastName = models.CharField(max_length=50)
    customerIdentityNumber = models.CharField(max_length=11)
    customerPhoneNumber = models.CharField(max_length=20)
    customerBirthDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.customerName

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    categoryPrice = models.IntegerField()
    def __str__(self):
        return self.categoryName


class Room(models.Model):
    roomNumber = models.CharField(max_length=50)
    capacity = models.IntegerField()
    roomStatus = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.roomNumber

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    entryDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    exitDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    bill = models.IntegerField()

    # here is the place where calculate the bill
    # def bill_calculate():