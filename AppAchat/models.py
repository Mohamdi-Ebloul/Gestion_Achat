from django.db import models
from Achateur import models as pmodels


class Stock(models.Model):
    Produit_name = models.CharField(max_length=10)
    Quantite = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Produit_name


class adminRequest(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    request_by_Achateur = models.ForeignKey(pmodels.Achateur, null=True, on_delete=models.CASCADE)
    Achateur_name = models.CharField(max_length=30,default="Achateur")
    Produit_name = models.ForeignKey(pmodels.Produit, null=True, on_delete=models.CASCADE)

    Fourniseur_name = models.ForeignKey(pmodels.Fournisseur, null=True, on_delete=models.CASCADE)
    societe = models.CharField(max_length=500,default="my socite")

    Prix = models.PositiveIntegerField()
    Quantite = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Produit_name
 
    def save(self, *args, **kwargs):
        if not self.id:
            last_id = adminRequest.objects.order_by('-id').first()
            if last_id:
                last_id_number = int(last_id.id[5:])
                # On récupère le dernier id enregistré et on extrait le nombre après le préfixe "P2023"
            else:
                last_id_number = 0
            new_id_number = last_id_number + 1
            new_id = "P2023{:04d}".format(new_id_number)
            # On incrémente le nombre et on ajoute le préfixe "P2023"
            self.id = new_id
        super(adminRequest, self).save(*args, **kwargs)


