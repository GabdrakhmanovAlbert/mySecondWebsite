from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.

def main_page(request):
    return render(request, './index.html')

def first_page(request):
    object_list = Order.objects.all()
    return render(request, './first.html', {'object_list': object_list})

def second_page(request):
    return render(request, './second.html')

def thanks_page(request):
    if len(request.POST) > 0:
        name = 'Undefind' if request.POST['name'] == '' else request.POST['name']
        phone = request.POST['phone']
    else:
        name = request.GET['name']
        phone = request.GET['phone']
    Order(order_name=name, order_phone=phone).save()
    return render(request, './thanks.html', {'name': name, 'phone': phone})

def third_page(request):
    form = OrderForm()
    return render(request, './third.html', {'form': form})

def fourth_page(request):
    return render(request, './base.html')

def fourth_page1(request):
    return render(request, './fourth1.html')

def fourth_page2(request):
    return render(request, './fourth2.html')

def fourth_page3(request):
    return render(request, './fourth3.html')

def fifth_page(request):
    return render(request, './fifth.html')