from django.shortcuts import render
from .forms import Register
# Create your views here.
def reg(request):
    f=Register()
    return render(request,'reg.html',{'forms':f})
