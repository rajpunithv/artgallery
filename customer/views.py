from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.template.context_processors import request

from .forms import FeedbackForm
from .models import Login, Customer, Feedback
from django.shortcuts import render, redirect
from .forms import FileUploadForm



# Create your views here.
def customerhome(request):
    return render(request, 'customerhome.html')


def logout(request):
    return render(request, 'index.html')


def checkcustomerlogin(request):
    adminuname = request.POST.get("uname")  # Use get method to avoid KeyError
    adminpwd = request.POST.get("pwd")  # Use get method to avoid KeyError

    if adminuname is not None and adminpwd is not None:
        # Assuming that your Login model has fields 'username' and 'password'
        flag = Login.objects.filter(username=adminuname, password=adminpwd).exists()
        if flag:
            return render(request, 'customerhome.html')
        else:
            msg = "Wrong details. Please enter correct username and password."
            return render(request, "wrongcustomer.html", {"message": msg})
    else:
        msg = "Please provide both username and password."
        return render(request, "customerlogin.html", {"message": msg})

def customerpayments(request):
    return render(request, "customerpayments.html")

def customergallery(request):
    return render(request, "customergallery.html")

def signup(request):
    return render(request, "signup.html")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # If the user is authenticated, capture their name
            if request.user.is_authenticated:
                form.instance.name = request.user.username

            form.save()
            return render(request, 'success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_list(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'feedback_list.html', {'feedback_entries': feedback_entries})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html',{'form':form})