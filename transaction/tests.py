from django.test import TestCase
from .models import Transaction
from datetime import date

class TransactionTestCase(TestCase):
    def setUp(self):
        self.high=Transaction.objects.create(_type      = 'Incasso',
                                            amount      = 9867256.99,
                                            date        = date(2020,11,11),
                                            name        = 'Test Trans',
                                            description = 'awdn awdhjaiwdb awdawd',
                                            category    = 'Groceries')
        self.low=Transaction.objects.create(_type       = 'Sundries',
                                            amount      = 0.01,
                                            date        = date(2019,3,14),
                                            name        = 'Test Trans',
                                            category    = 'Liabilities')
        self.norm=Transaction.objects.create(_type      = 'Transfer',
                                            amount      = 97.52,
                                            date        = date(2077,5,22),
                                            name        = 'Whatever')
        self.neg=Transaction.objects.create(_type       = 'SEPA direct debit',
                                            amount      = -71249.82,
                                            date        = date(1997,10,3),
                                            name        = 'Filler')

    def test_ordering(self):
        qs = Transaction.objects.all()
        self.assertEqual(qs.count(), 4)
        self.assertEqual(qs[0].date, date(2077,5,22))
        self.assertEqual(qs[1].date, date(2020,11,11))
        self.assertEqual(qs[2].date, date(2019,3,14))
        self.assertEqual(qs[3].date, date(1997,10,3))
