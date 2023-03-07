from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from AppAchat.models import Stock,adminRequest
import json
# Create your tests here.


class TestViews(TestCase):
    def test_Myapp(self):
        client=Client()

        response = client.get(reverse('home'))


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/index.html')