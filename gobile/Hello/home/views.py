from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
def index(request):
 #   context = 1
    return render(request,'index1.html')
#    return HttpResponse("this is jisoo")



def bp(request):
    return HttpResponse("black pink")
def about(request):
    return render(request,'about.html')
def contact(request):

    print("we are using post request")

   
    if request.method == "POST":    
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        print(name,email,desc)
        messages.success(request, 'respones has been sent!')
    
    return render(request,'contact.html')

    
# Create your views here.
