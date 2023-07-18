from django.shortcuts import render, redirect

from Analyst.models import ReadOnlyDocument
from .forms import DocumentForm
from .models import Document
from .encryption import encrypt_file, decrypt_file
from cryptography.fernet import Fernet
from authentication.models import User
from django.utils import timezone
from blockchain.models import  Blockchain, BlockchainManager, hashGenerator

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
            # Generate a random encryption key
            key = Fernet.generate_key()
            print("Key",key)
            # Encrypt a file
            file_path = file1
            enc_file = encrypt_file(file_path, key)
            # Process the file as needed (e.g., save it, manipulate it, etc.)
            # Example: Save the file to a Document model
            document = Document(owner=user,file=enc_file, key=key)
            document.save()
            return redirect('owner')  # Redirect to a success page
    else:
        print("Dhukse NAAAA")
        form = DocumentForm()
    
    return render(request, 'UploadDocument.html', {'form': 'form'})

def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'document_list.html', {'documents': documents})


def send_document(request):
    if request.method == 'POST':
        print("hi")
        send_user = request.user
        document = request.POST.get('document')
        receive_user = request.POST.get('user')
        hash_key = request.POST.get('hash_key')
        post_time = timezone.now()
        operation = request.POST.get('operation')
        idx = 0
        print(document)

        file1 = decrypt_file(document,key=hash_key)
        read_only_doc = ReadOnlyDocument(owner=send_user,file=file1)
        read_only_doc.save()
        data1 = {
            'send_user' : send_user,
            'receive_user' : receive_user,
            'document' : document,
            'operation' : operation,
            'post_time' : post_time
        }
        blocks = Blockchain.objects.filter()
        print("1",blocks)
        print(blocks[len(blocks)-1])
        prev_block = blocks[len(blocks)-1]
        curr_hash = hashGenerator(data1['document'])
        prev_hash = prev_block.hash
        b = Blockchain(data=data1, hash=curr_hash, prev_hash=prev_hash)
        b.save()
        return redirect('owner') 

    else : 
        documents = Document.objects.filter(owner=request.user)
        users = User.objects.filter(is_analyst=True)
        context = {
            'documents' : documents,
            'users': users
        }
        return render(request, 'SendDocument.html', context)
