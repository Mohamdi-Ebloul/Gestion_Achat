from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum, Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from AppAchat import forms as bforms
from AppAchat import models as bmodels


def Achateur_signup_view(request):
    userForm = forms.AchateurUserForm()
    AchateurForm = forms.AchateurForm()
    mydict = {'userForm': userForm, 'AchateurForm': AchateurForm}
    if request.method == 'POST':
        userForm = forms.AchateurUserForm(request.POST)
        AchateurForm = forms.AchateurForm(request.POST, request.FILES)
        if userForm.is_valid() and AchateurForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            Achateur = AchateurForm.save(commit=False)
            Achateur.user = user
            Achateur.save()
            my_Achateur_group = Group.objects.get_or_create(name='Achateur')
            my_Achateur_group[0].user_set.add(user)
        return HttpResponseRedirect('Achateurlogin')
    return render(request, 'Achateur/Achateursignup.html', context=mydict)


def Achateur_dashboard_view(request):
    Achateur = models.Achateur.objects.get(user_id=request.user.id)
    dict = {
        'requestpending': bmodels.adminRequest.objects.all().filter(request_by_Achateur=Achateur).filter(
            status='Pending').count(),
        'requestapproved': bmodels.adminRequest.objects.all().filter(request_by_Achateur=Achateur).filter(
            status='Approved').count(),
        'requestmade': bmodels.adminRequest.objects.all().filter(request_by_Achateur=Achateur).count(),
        'requestrejected': bmodels.adminRequest.objects.all().filter(request_by_Achateur=Achateur).filter(
            status='Rejected').count(),

    }

    return render(request, 'Achateur/Achateur_dashboard.html', context=dict)


def make_request_view(request,pk):
    request_form = bforms.RequestForm()
    user = models.User.objects.get(id=pk)
    userForm = forms.AchateurUserForm(instance=user)
    if request.method == 'POST':
        request_form = bforms.RequestForm(request.POST)
        if request_form.is_valid():
            admin_request = request_form.save(commit=False)
            admin_request.Produit_name = request_form.cleaned_data['Produit_name']
            user = models.User.objects.get(id=pk)
            admin_request.Achateur_name =user.last_name
            
            Achateur = models.Achateur.objects.get(user_id=request.user.id)
            admin_request.request_by_Achateur = Achateur
            admin_request.save()
            return redirect('admin-request')
    return render(request, 'Achateur/makerequest.html', {'request_form': request_form,'userForm':userForm})


def my_request_view(request):
    Achateur = models.Achateur.objects.get(user_id=request.user.id)
    admin_request = bmodels.adminRequest.objects.all().filter(request_by_Achateur=Achateur)
    return render(request, 'Achateur/my_request.html', {'admin_request': admin_request})
