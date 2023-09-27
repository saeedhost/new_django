from django.http import HttpResponse
from django.shortcuts import render
from contactForm.models import contactFields

def form(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        web_link=request.POST.get('weblink')
        country=request.POST.get('country')
        message=request.POST.get('message')

        insertFormData=contactFields(Name=name,Email=email,Phone=phone,Website_Link=web_link,Country=country,Message=message)
        insertFormData.save()
    return render(request, "form.html")

def showformdata(request):
    formAlldata=contactFields.objects.all()
    return render(request, "getFormData.html", {'alldata': formAlldata})