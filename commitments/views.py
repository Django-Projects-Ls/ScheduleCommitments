from .models import Commitment
from django.shortcuts import redirect, render
from .forms import CommitmentsForms
from django.db.models import Q

def commitments_request_handler(request):
    dados = {}
    query = request.GET.get('q')
    print(query)
    if query:
        dados['query'] = query
        queryset = (Q(data__icontains=query))
        items = Commitment.objects.filter(queryset).distinct()
    else:
        items = Commitment.objects.all()
    
    dados['commitment'] = items
    return render(request, 'index.html', dados)

def details_request_handler(request, id):
    return render(request, 'details.html', {'commitment' : Commitment.objects.get(id=id)})

def create_commitment(request):
    if request.method == "POST":
        form = CommitmentsForms(request.POST) # Getting our params of our request
        
        if form.is_valid():
            form.save()
        
        return redirect('/')
    
    elif request.method == "GET":
        form = CommitmentsForms()
        return render(request, 'form.html', {'form' : form})

def edit_commitment(request, pk):
    commitment = Commitment.objects.get(id=pk)
    
    if request.method == "POST":
        form = CommitmentsForms(request.POST, instance=commitment)
        
        if form.is_valid():
            form.save()
        
        return redirect('/')
    
    else:
        form = CommitmentsForms(instance=commitment)
        return render(request, 'form.html', {'form' : form})

def delete_commitment(request, pk):
    commitment = Commitment.objects.get(id=pk)
    commitment.delete()
    
    return render(request, 'excluir.html')