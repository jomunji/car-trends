from django.shortcuts import render
# Create your views here.

#This function renders the home.html file when called.
def home(request): #The request argument is created whenever a page loads, it contains metadata
    return render(request,"home/home.html", {})