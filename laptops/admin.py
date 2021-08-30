from django.contrib import admin
from .models import Laptop

# Register your models here.
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'hard', 'ram', 'cpu')
