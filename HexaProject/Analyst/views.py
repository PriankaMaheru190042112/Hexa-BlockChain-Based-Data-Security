from django.shortcuts import render
from .models import ReadOnlyDocument

# Create your views here.
def analyst_home(request):
    return render (request,'Analyst/AnalystHome.html')

def view_pdf(request):
    return render (request, 'Analyst/ViewPDF.html')

def permitted_files(request):
    user = request.user
    print(user)
    files = ReadOnlyDocument.objects.filter(reader=user)
    print(files)
    return render (request, 'Analyst/PermittedFiles.html', {'files':files})