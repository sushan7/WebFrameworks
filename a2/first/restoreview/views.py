from django.shortcuts import render
from django.http import HttpResponse
from . models import restoinfo

# Create your views here.
def index(request):
    #return HttpResponse("<h2> hdhdg </h2>")
    return render(request,"restoreview/index.html")

def addresto(request):
    return render(request,"restoreview/add_resto.html")

def add_resto_form_submission(request):
    resto_name = request.POST["resto_name"]
    resto_type = request.POST["resto_type"]
    resto_review = request.POST["resto_review"]
    resto_detail = request.POST["resto_detail"]

    resto_info = restoinfo(resto_name = resto_name,resto_type = resto_type,resto_review = resto_review,resto_detail = resto_detail)
    resto_info.save()
    return render(request,"restoreview/add_resto.html")
