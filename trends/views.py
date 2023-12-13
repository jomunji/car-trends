from django.shortcuts import render

# Create your views here.
def trends(request):
    return render(request,'trends/trends.html',{})