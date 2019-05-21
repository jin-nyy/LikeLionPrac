from django.shortcuts import render
from .models import PortFolio
# Create your views here.
def home(request):
    portfolio = PortFolio.objects.all()

    return render(request,'portfolio/home.html',{'portfolio':portfolio})