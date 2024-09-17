from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def gallery(request):
    return render(request,"gallery.html")

def payments(request):
    return render(request,"payments.html")

def artistlogin(request):
    return render(request,"artistlogin.html")

def customerlogin(request):
    return render(request,"customerlogin.html")

def feedback1(request):
    return render(request,"feedback1.html")

def checkmethod(request):
    if request.method == 'POST':
        selected_method = request.POST.get('payment-method')

        if selected_method == 'credit/debit-card':
            return HttpResponseRedirect('creditcard')

        if selected_method == 'net-banking':
            return HttpResponseRedirect('debitcard')

        if selected_method == 'cod':
            return HttpResponseRedirect('cod')

        if selected_method == 'qr-scanner':
            return HttpResponseRedirect('qrcode')



def creditcard(request):
    return render(request,"creditcard.html")

def debitcard(request):
    return render(request,"debitcard.html")

def qrcode(request):
    return render(request,"qrcode.html")

def cod(request):
    return render(request,"cod.html")
