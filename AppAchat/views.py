from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from Achateur import models as pmodels
from Achateur import forms as pforms


def home_view(request):
   

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'admin/index.html')



def is_Achateur(user):
    return user.groups.filter(name='Achateur').exists()


def afterlogin_view(request):
    if is_Achateur(request.user):
        return redirect('admin-dashboard')
    else:
        return redirect('admin-dashboard')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    totalunit = models.Stock.objects.aggregate(Sum('Quantite'))
    valeurs=models.adminRequest.objects.aggregate(Sum('Prix'))
    valeurmoyen=valeurs['Prix__sum']
    if valeurmoyen !=None:
      v=valeurmoyen/models.adminRequest.objects.all().count(),
      
    else:
      v=0
        
    dict = {   
        'totaladminunit': totalunit['Quantite__sum'],
        'totalrequest': models.adminRequest.objects.all().count(),
        'totalapprovedrequest': models.adminRequest.objects.all().filter(status='Approved').count(),
        'valeurmoyen':v, 
        'requests' :models.adminRequest.objects.all()

    }
    return render(request, 'admin/admin_dashboard.html', context=dict)





@login_required(login_url='adminlogin')
def admin_Achateur_view(request):
    Achateurs = pmodels.Achateur.objects.all()
    return render(request, 'admin/admin_Achateur.html', {'Achateurs': Achateurs})

def prfile_view(request):
    Achateurs = pmodels.Achateur.objects.all()
    return render(request, 'admin/profil.html', {'Achateurs': Achateurs})

@login_required(login_url='adminlogin')
def admin_Fournisseur_view(request):
    Fournisseurs = pmodels.Fournisseur.objects.all()
    return render(request, 'admin/admin_Fournisseur.html', {'Fournisseurs': Fournisseurs})

@login_required(login_url='adminlogin')
def admin_Produit_view(request):
    Produits = pmodels.Produit.objects.all()
    return render(request, 'admin/admin_Produit.html', {'Produits': Produits})






@login_required(login_url='adminlogin')
def Fournisseur_signup_view(request):
    fournisseurForm=pforms.FournisseurForm()

    mydict={'fournisseurForm':fournisseurForm}
    if request.method=='POST':
        fournisseurForm=pforms.FournisseurForm(request.POST,request.FILES)

        if fournisseurForm.is_valid():

            fournisseur=fournisseurForm.save(commit=False)

            fournisseur.email=fournisseurForm.cleaned_data['email']
            fournisseur.save()
          

        return HttpResponseRedirect("admin-Fournisseur")
    return render(request,'admin/fournisseuradd.html',context=mydict)

@login_required(login_url='adminlogin')
def Produit_signup_view(request):
    produitForm=pforms.ProduitForm()

    mydict={'produitForm':produitForm}
    if request.method=='POST':
        produitForm=pforms.ProduitForm(request.POST,request.FILES)

        if produitForm.is_valid():

            produit=produitForm.save(commit=False)

            produit.nom=produitForm.cleaned_data['nom']
            produit.save()
          

        return HttpResponseRedirect("admin-Produit")
    return render(request,'admin/produitadd.html',context=mydict)

@login_required(login_url='adminlogin')
def update_Achateur_view(request, pk):
    Achateur = pmodels.Achateur.objects.get(id=pk)
    user = pmodels.User.objects.get(id=Achateur.user_id)
    userForm = pforms.AchateurUserForm(instance=user)
    AchateurForm = pforms.AchateurForm( instance=Achateur)
    mydict = {'userForm': userForm, 'AchateurForm': AchateurForm}
    if request.method == 'POST':
        userForm = pforms.AchateurUserForm(request.POST, instance=user)
        AchateurForm = pforms.AchateurForm(request.POST, request.FILES, instance=Achateur)
        if userForm.is_valid() and AchateurForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            Achateur = AchateurForm.save(commit=False)
            Achateur.user = user
            Achateur.save()
            return redirect('admin-Achateur')
    return render(request, 'admin/update_Achateur.html', context=mydict)


@login_required(login_url='adminlogin')
def update_Fournisseur_view(request, pk):
    fournisseur = pmodels.Fournisseur.objects.get(id=pk)
    fournisseurForm = pforms.FournisseurForm(instance=fournisseur)
    mydict = {'fournisseurForm': fournisseurForm}
    if request.method == 'POST':
        fournisseurForm = pforms.FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        if fournisseurForm.is_valid():
           
            fournisseur = fournisseurForm.save(commit=False)
            fournisseur.nom = fournisseurForm.cleaned_data['nom']
            fournisseur.save()
            return redirect('admin-Fournisseur')
    return render(request, 'admin/update_Fournisseur.html', context=mydict)


@login_required(login_url='adminlogin')
def update_Produit_view(request, pk):
    produit = pmodels.Produit.objects.get(id=pk)
    produitForm = pforms.ProduitForm(instance=produit)
    mydict = {'produitForm': produitForm}
    if request.method == 'POST':
        produitForm = pforms.ProduitForm(request.POST, request.FILES, instance=produit)
        if produitForm.is_valid():
           
            produit = produitForm.save(commit=False)
            produit.nom = produitForm.cleaned_data['nom']
            produit.save()
            return redirect('admin-Produit')
    return render(request, 'admin/update_Produit.html', context=mydict)


@login_required(login_url='adminlogin')
def delete_Achateur_view(request, pk):
    Achateur = pmodels.Achateur.objects.get(id=pk)
    user = User.objects.get(id=Achateur.user_id)
    user.delete()
    Achateur.delete()
    return HttpResponseRedirect('/admin-Achateur')


@login_required(login_url='adminlogin')
def delete_Fournissur_view(request, pk):
    Fournisseur = pmodels.Fournisseur.objects.get(id=pk)
    Fournisseur.delete()
    return HttpResponseRedirect('/admin-Fournisseur')

@login_required(login_url='adminlogin')
def delete_Produit_view(request, pk):
    Produit = pmodels.Produit.objects.get(id=pk)
    Produit.delete()
    return HttpResponseRedirect('/admin-Produit')


@login_required(login_url='adminlogin')
def admin_request_view(request):
    requests = models.adminRequest.objects.all().filter(status='Pending')
    return render(request, 'admin/admin_request.html', {'requests': requests})


@login_required(login_url='adminlogin')
def admin_request_history_view(request):
    requests = models.adminRequest.objects.all().exclude(status='Pending')
    return render(request, 'admin/admin_request_history.html', {'requests': requests})




@login_required(login_url='adminlogin')
def update_approve_status_view(request, pk):
    req = models.adminRequest.objects.get(id=pk)
    message = None
    
    req.status = "Approved"
    req.save()

    requests = models.adminRequest.objects.all().filter(status='Pending')
    return render(request, 'admin/admin_request.html', {'requests': requests, 'message': message})


@login_required(login_url='adminlogin')
def update_reject_status_view(request, pk):
    req = models.adminRequest.objects.get(id=pk)
    req.status = "Rejected"
    req.save()
    return HttpResponseRedirect('/admin-request')
