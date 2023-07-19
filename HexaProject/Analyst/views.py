from django.shortcuts import render
from .models import ReadOnlyDocument
from django.shortcuts import get_object_or_404
import os
from django.http import HttpResponse

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


def download_file(request):
    document = ReadOnlyDocument.objects.filter(reader=request.user)
    print('document',document[len(document)-1].file)
    file_path = str(document[len(document)-1].file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response

    return HttpResponse("File not found.", status=404)