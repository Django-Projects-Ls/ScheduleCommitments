from .models import Commitment
from django.shortcuts import redirect, render
from .forms import CommitmentsForms

def commitments_request_handler(request):
    return render(request, 'index.html', {'commitment' : Commitment.objects.all().values()})

def details_request_handler(request, id):
    return render(request, 'details.html', {'commitment' : Commitment.objects.get(id=id)})

def create_commitment(request):
    if request.method == "POST":
        form = CommitmentsForms(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('/')
    
    elif request.method == "GET":
        form = CommitmentsForms()
        return render(request, 'form.html', {'form' : form})