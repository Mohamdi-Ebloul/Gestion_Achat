from django.db import models
from django.contrib.auth.models import User


class Achateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name
    


   
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
    

class Commande(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_commande = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)



class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()

    def __str__(self):
        return self.nom
    
    def get_prix_total(self, quantite):
        return self.prix_unitaire * quantite

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def get_prix_total(self):
        return self.prix_unitaire * self.quantite