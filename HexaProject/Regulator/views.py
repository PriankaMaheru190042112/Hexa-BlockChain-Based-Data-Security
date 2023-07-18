from django.shortcuts import render

# Create your views here.
def regulator_home(request):
    return render(request, "Regulator/RegulatorHome.html")