from django.shortcuts import render
from django.contrib.auth.models import User
from mainApp.models import *
from django.core.paginator import Paginator

# Create your views here.

def adminLoginView(request):
    return render(request, "admin_login.html")




def get_adminpanel_url(request):
    orders = Checkout.objects.all().order_by('-id')
    count_order = Checkout.objects.all().count()
    count_offers = Offer.objects.all().count()

    completed_orders = Checkout.objects.filter(is_complete=True).count()

    increase = completed_orders / 100

    orders_paginator = Paginator(orders, 10)

    page_number = request.GET.get('page')

    orders_obj = orders_paginator.get_page(page_number)

    args = {
        "orders": orders,
        "orders_obj": orders_obj,
        "count_order": count_order,
        "count_offers": count_offers,
        "increase": increase
    }
    return render(request, 'admin_panel.html', args)


def order_details(request, id):
    order_details = Checkout.objects.get(pk=id)

    args = {
        "order_details": order_details
    }

    return render(request, "admin_order_Details.html", args)




def uploadedOfferView(request):
    all_offers = Offer.objects.all().order_by('-id')

    args = {
        "all_offers": all_offers
    }
    return render(request, "uploaded_offer.html", args)



def allUsersView(request):
    users = User.objects.exclude(username=request.user).order_by('-id')

    args = {
        "users": users
    }

    return render(request, "all_users.html", args)



def allOrdersView(request):
    orders = Checkout.objects.all().order_by('-id')
    args = {
        "orders": orders
    }
    return render(request, "all_order.html", args)



def adminLoginView(request):
    return render(request, "admin_login.html")



def transactionView(request):
    transactions = Checkout.objects.filter(paid=True)
    completed_orders = Checkout.objects.filter(is_complete=True).count()
    increase = (completed_orders / 100)
    args = {
        'transactions': transactions,
        'increase': increase
    }
    return render(request, "transactions.html", args)
