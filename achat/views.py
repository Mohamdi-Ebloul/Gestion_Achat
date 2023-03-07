
# Create your views here.
from django.shortcuts import render
from .models import Produit

def accueil(request):
    return render(request, 'achat/accueil.html')

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'achat/liste_produits.html', {'produits': produits})


from django.shortcuts import redirect
from django.contrib import messages

def ajouter_au_panier(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    panier = request.session.get('panier', {})
    quantite = panier.get(produit_id, 0) + 1
    panier[produit_id] = quantite
    request.session['panier'] = panier
    messages.success(request, f"{produit.nom} a été ajouté à votre panier.")
    return redirect('liste_produits')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Commande, LigneCommande

def passer_commande(request):
    if request.method == 'POST':
        commande = Commande.objects.create(
            utilisateur=request.user,
            adresse_livraison=request.POST.get('adresse_livraison'),
            ville_livraison=request.POST.get('ville_livraison'),
            code_postal_livraison=request.POST.get('code_postal_livraison')
        )
        panier = request.session.get('panier', {})
        for produit_id, quantite in panier.items():
            produit = Produit.objects.get(id=produit_id)
            LigneCommande.objects.create(
                commande=commande,
                produit=produit,
                quantite=quantite,
                prix_unitaire=produit.prix
            )
        del request.session['panier']
        messages.success(request, 'Votre commande a été passée avec succès.')
        return redirect('liste_produits')
    else:
        return render(request, 'achat/passer_commande.html')
