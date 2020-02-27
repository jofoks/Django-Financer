from django.test import TestCase
from django.db import IntegrityError
from envelope.models import fixedCharge, incomeFraction

class incomeFractionTestCase(TestCase):
    def setUp(self):
        self.frac_high=incomeFraction.objects.create(name='High', description='yeet', amount=99.99)
        self.frac_low=incomeFraction.objects.create(name='Low', amount=0.01)
        self.frac_norm=incomeFraction.objects.create(name='Norm', amount=10)
        self.frac_neg=incomeFraction.objects.create(name='Neg', amount=-14.13)

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
        self.charge_high=fixedCharge.objects.create(name='High', description='yeet', amount=50123.99)
        self.charge_low=fixedCharge.objects.create(name='Low', amount=0.01)
        self.charge_norm=fixedCharge.objects.create(name='Norm', amount=23.55)
        self.charge_neg=fixedCharge.objects.create(name='Neg', amount=-14.13)

    def test_ordering(self):
        qs = fixedCharge.objects.all()
        self.assertEqual(qs.count(), 4)
        self.assertEqual(qs[0].name, 'High')
        self.assertEqual(qs[1].name, 'Norm')
        self.assertEqual(qs[2].name, 'Low')
        self.assertEqual(qs[3].name, 'Neg')

    def test_unique_name(self):
        self.assertRaises(IntegrityError, fixedCharge.objects.create, name='High', amount=0)
