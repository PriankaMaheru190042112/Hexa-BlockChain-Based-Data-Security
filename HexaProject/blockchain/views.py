from django.shortcuts import render
from .ledger import Blockchain, block


# Create your views here.
def ledger(request):
    bc=Blockchain()
    bc.add_block('1')
    bc.add_block('2')
    bc.add_block('3')

    for block in bc.chain:
        print(block.__dict__)
    return render(request, 'blockchain/ledger.html')

def logbook(request):
    return render(request, 'blockchain/logbook.html')

