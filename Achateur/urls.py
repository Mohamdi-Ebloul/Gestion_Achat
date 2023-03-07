from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('Achateurlogin', LoginView.as_view(template_name='Achateur/Achateurlogin.html'),name='Achateurlogin'),
    path('Achateursignup', views.Achateur_signup_view,name='Achateursignup'),
    path('Achateur-dashboard', views.Achateur_dashboard_view,name='Achateur-dashboard'),
    path('make-request/<int:pk>', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
]