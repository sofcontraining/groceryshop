from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html")
def shopgrid(request):
    return render(request, 'shop-grid.html')
