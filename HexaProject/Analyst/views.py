from django.shortcuts import render

# Create your views here.
def analyst_home(request):
    return render (request,'Analyst/AnalystHome.html')