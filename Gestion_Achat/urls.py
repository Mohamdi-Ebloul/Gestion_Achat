from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
from django.contrib.auth.views import LogoutView,LoginView
from AppAchat import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('Achateur/', include('Achateur.urls')),

    path('', views.home_view, name='home'),
    path('logout', LogoutView.as_view(template_name='admin/logout.html'), name='logout'),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='admin/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-Achateur', views.admin_Achateur_view, name='admin-Achateur'),
    path('profile', views.prfile_view, name='profile'),
    path('admin-Fournisseur', views.admin_Fournisseur_view, name='admin-Fournisseur'),
        path('admin-Produit', views.admin_Produit_view, name='admin-Produit'),

    path('fournisseuradd', views.Fournisseur_signup_view,name='fournisseuradd'),

    path('produitadd', views.Produit_signup_view,name='produitadd'),
    path('admin-request', views.admin_request_view, name='admin-request'),
    path('update-Achateur/<int:pk>', views.update_Achateur_view, name='update-Achateur'),
path('update-Fournisseur/<int:pk>', views.update_Fournisseur_view, name='update-Fournisseur'),

path('update-Produit/<int:pk>', views.update_Produit_view, name='update-Produit'),
    path('delete-Achateur/<int:pk>', views.delete_Achateur_view, name='delete-Achateur'),

    path('delete-Fournissur/<int:pk>', views.delete_Fournissur_view, name='delete-Fournissur'),
path('delete-Produit/<int:pk>', views.delete_Produit_view, name='delete-Produit'),
    path('admin-request-history', views.admin_request_history_view, name='admin-request-history'),
    path('update-approve-status/<str:pk>', views.update_approve_status_view, name='update-approve-status'),
    path('update-reject-status/<str:pk>', views.update_reject_status_view, name='update-reject-status'),

]
