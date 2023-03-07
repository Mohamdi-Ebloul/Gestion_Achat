from django.urls import path
from achat.views import *

urlpatterns = [
    path('', accueil, name='accueil'),
     path('liste_produits/', liste_produits, name='liste_produits'),
 path('panier/ajouter/<int:produit_id>/', ajouter_au_panier, name='ajouter_au_panier'),
 path('commande/passer/', passer_commande, name='passer_commande')
]
