from django.shortcuts import render

# Create your views here.
def manufacturers(request):
    return render(request,'manufacturers/manufacturers.html',{})
