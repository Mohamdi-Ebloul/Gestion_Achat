from django import forms
from django.contrib.auth.models import User
from . import models


class AchateurUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class AchateurForm(forms.ModelForm):
    class Meta:
        model = models.Achateur
        fields = [ 'email', 'address','mobile', ]

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = models.Fournisseur
        fields = ['nom', 'adresse', 'email', 'telephone']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = models.Produit
        fields = ['nom', 'description','prix_unitaire','quantite_stock']