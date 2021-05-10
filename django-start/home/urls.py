from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home1'),
    path('home/',views.home,name='home2'),
    path('reservation/',views.reservation,name='reservation'),

    path('room/<roomnum>/', views.room_detail, name='room_detail'),
    path('about/',views.about,name='about')
]
