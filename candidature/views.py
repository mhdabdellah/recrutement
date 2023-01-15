from django.shortcuts import render
from .forms import CandidatureForm
from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from poste.models import Poste

# Create your views here.

def index(request):
    postes =Poste.objects.all()
    i = 1
    for p in postes:
        print(i)
        i+=1

    context={
        'postes':postes
    }
    
    return render(request, 'candidature/postes.html',context)

def candidatureForm(request,poste_id):
    poste =Poste.objects.get(id = poste_id)
    if request.method == 'POST':
        candidature_Form = CandidatureForm(request.POST, request.FILES)
        if candidature_Form.is_valid():
            form = form.save(commit=False)
            form.poste = poste
            candidature_Form.save()
            messages.success( 
                # {myform.nom}/{myform.prenom}
                request, f"Felicitations Votre Candidature est bien Récu")
            return redirect(reverse('candidature:postes'))
    else:
        candidature_Form = CandidatureForm()
        context={
           
            'candidature_Form' : candidature_Form,

        }
        return render(request,'candidature/candidatureform.html',context)

