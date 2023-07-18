from django.shortcuts import render

# Create your views here.
def ledger(request):
    return render(request, 'blockchain/ledger.html')