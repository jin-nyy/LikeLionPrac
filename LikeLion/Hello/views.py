from django.shortcuts import render

def HelloWorld(request):
    return render(request, 'HelloWorld.html')
# Create your views here.
