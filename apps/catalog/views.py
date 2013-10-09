from django.shortcuts import render
from catalog.models import Festival

def index(request):
    return render(request, "index.html")

def list(request):
    filter = request.GET['filter'] if request.GET['filter'] else ''
    try:
        order, direction = request.GET['order'].split('-')
    except ValueError:
        order = 'name'
        direction = ''
    if order not in ['name', 'date_start']:
        order = 'name'
    if direction == 'desc':
        direction = '-'
    else:
        direction = ''
    festivals = Festival.objects.filter(name__icontains=filter).order_by(direction+order)
    return render(request, "list.html", {'festivals': festivals})
