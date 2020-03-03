from django.test import TestCase
from django.db import IntegrityError
from bankAccounts.models import US_Account, NL_Account
from address.models import Address
from django.contrib.auth.models import User

class US_AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.dummyAddress= Address.objects.create(raw='123 UrTest Lane, Tester, 90111 TE, United Test')
        self.savings=US_Account.objects.create(address= self.dummyAddress ,routingNumber=999999999 ,accountNumber=1010101010 ,accountType='Savings', owner=self.user)
        self.checkings=US_Account.objects.create(address= self.dummyAddress ,routingNumber=862946719 ,accountNumber=121212121212 ,accountType='Checkings', owner=self.user)

    def test_unique_name(self):
        self.assertRaises(IntegrityError, US_Account.objects.create, address= self.dummyAddress ,routingNumber=0 ,accountNumber=121212121212 ,accountType='Checkings')

class NL_AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.one=NL_Account.objects.create(name='Mister Test', AccountNumber='INGB343434343434343434343434343434', owner=self.user)
        self.two=NL_Account.objects.create(name='Miss Tester', AccountNumber='ABNA9876141982', owner=self.user)

    def test_unique_name(self):
        self.assertRaises(IntegrityError, NL_Account.objects.create, name='Mister Test', AccountNumber='**', owner=self.user)
        
    def test_unique_number(self):
        self.assertRaises(IntegrityError, NL_Account.objects.create, name='**', AccountNumber='ABNA9876141982', owner=self.user)

