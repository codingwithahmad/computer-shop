from django.shortcuts import render
from django.views.generic import ListView
from .models import Laptop

# Create your views here.

class Home(ListView):
	model = Laptop

	


