from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

# Create your views here.
def owner_home(request):
    return render(request , 'OwnerHome.html')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        file = request.POST['file']
        owner = request.user
        print(file)
        print(owner)
        if form.is_valid():
            owner = request.user
            print(owner)
            file = form.cleaned_data['file']
            Document.objects.create(owner=owner, file=file)
            return redirect('document_list')  # Redirect to a success page
    else:
        form = DocumentForm()
    
    return render(request, 'UploadDocument.html', {'form': form})

def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'document_list.html', {'documents': documents})

