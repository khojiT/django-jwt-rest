from django.shortcuts import render
from .models import employee,product
def index(request):
    emp = employee.objects.all()
    pro = product.objects.all()
    return render(request,'index.html',{'emp':emp,'pro':pro})
    
