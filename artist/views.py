from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect

from .forms import FileUploadForm
from .models import Login,Artist


# Create your views here.
def artisthome(request):
    return render(request, 'artisthome.html')


def logout(request):
    return render(request, 'index.html')


def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag = Login.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["auname"]=adminuname
        return render(request,'artisthome.html',{"adminuname":adminuname})
    else:
        msg = "Wrong details. Please enter correct username and password."
        return render(request, "wrongartist.html", {"message": msg})
        # return HttpResponse("Login Failed")


def uploadarts(request):
    return render(request, "uploadarts.html")

def artpayments(request):
    return render(request, "artpayments.html")

def artgallery(request):
    return render(request, "artgallery.html")

def signup(request):
    return render(request, "signup.html")

def artistchangepwd(request):
    return render(request, "artistchangepwd.html")


def customerchangepwd(request):
    return render(request, "customerchangepwd.html")

def artistupdatepwd(request):
    auname=request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(auname,opwd,npwd)
    flag=Artist.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("Old password is correct")
        Artist.objects.filter(username=auname).update(password=npwd)
        msg="Old password updated successfuly"
    else:
        print("Old password in Invalid")
        msg="Old password is incorrect"
    return render(request,"artistchangepwd.html",{"auname":auname,"message":msg})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html',{'form':form})