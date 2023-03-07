from django import forms

from . import models


class adminForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['Produit_name','Quantite']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.adminRequest
        fields=['Achateur_name','Produit_name','Fourniseur_name','Prix','Quantite',]



