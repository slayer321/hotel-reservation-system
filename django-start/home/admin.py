from django.contrib import admin
from .models import Adress,Customer,Category,Room,Bill
admin.site.register(Customer)
admin.site.register(Adress)
admin.site.register(Category)

class RoomAdmin(admin.ModelAdmin):
    list_display =('roomNumber','roomstatus') 

admin.site.register(Room,RoomAdmin)
admin.site.register(Bill)