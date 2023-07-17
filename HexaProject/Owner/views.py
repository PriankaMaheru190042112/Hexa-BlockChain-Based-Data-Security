from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

# Create your views here.
def owner_home(request):
    return render(request , 'OwnerHome.html')

def upload_document(request):
    if request.method == 'POST':
        print("Dhukse")
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("Dhukse")
            user = request.user
            file1 = request.FILES['file']
            # Process the file as needed (e.g., save it, manipulate it, etc.)
            # Example: Save the file to a Document model
            document = Document(owner=user,file=file1)
            document.save()
            return redirect('owner_home')  # Redirect to a success page
    else:
        print("Dhukse NAAAA")
        form = DocumentForm()
    
    return render(request, 'UploadDocument.html', {'form': 'form'})

def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'document_list.html', {'documents': documents})

