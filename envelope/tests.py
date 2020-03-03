from django.test import TestCase
from django.db import IntegrityError
from envelope.models import fixedCharge, incomeFraction
from django.contrib.auth.models import User

class incomeFractionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.frac_high=incomeFraction.objects.create(name='High', description='yeet', amount=99.99, owner= self.user)
        self.frac_low=incomeFraction.objects.create(name='Low', amount=0.01, owner= self.user)
        self.frac_norm=incomeFraction.objects.create(name='Norm', amount=10, owner= self.user)
        self.frac_neg=incomeFraction.objects.create(name='Neg', amount=-14.13, owner= self.user)

    def test_ordering(self):
        qs = incomeFraction.objects.all()
        self.assertEqual(qs.count(), 4)
        self.assertEqual(qs[0].name, 'High')
        self.assertEqual(qs[1].name, 'Norm')
        self.assertEqual(qs[2].name, 'Low')
        self.assertEqual(qs[3].name, 'Neg')

    def test_unique_name(self):
        self.assertRaises(IntegrityError, incomeFraction.objects.create, name='High', amount=0)

class fixedChargeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.charge_high=fixedCharge.objects.create(name='High', description='yeet', amount=50123.99, owner= self.user)
        self.charge_low=fixedCharge.objects.create(name='Low', amount=0.01, owner= self.user)
        self.charge_norm=fixedCharge.objects.create(name='Norm', amount=23.55, owner= self.user)
        self.charge_neg=fixedCharge.objects.create(name='Neg', amount=-14.13, owner= self.user)

    def test_ordering(self):
        qs = fixedCharge.objects.all()
        self.assertEqual(qs.count(), 4)
        self.assertEqual(qs[0].name, 'High')
        self.assertEqual(qs[1].name, 'Norm')
        self.assertEqual(qs[2].name, 'Low')
        self.assertEqual(qs[3].name, 'Neg')

    def test_unique_name(self):
        self.assertRaises(IntegrityError, fixedCharge.objects.create, name='High', amount=0, owner= self.user)
