from django.test import TestCase
from debt.models import Debt
from django.db import models
from contacts.models import Contact
from django.utils.timezone import now
from bankAccounts.models import NL_Account
from django.contrib.auth.models import User
import datetime
from django.contrib.contenttypes.models import ContentType

    # name        = models.CharField(max_length=256)
    # description = models.CharField(max_length=1024, blank=True)
    # amount      = models.DecimalField(max_digits=64, decimal_places=2)
    # creditor    = models.ForeignKey(Contact, on_delete=models.CASCADE)
    # dueDate     = models.DateField('Due Date', blank=True)
    # startDate   = models.DateField('Start Date', default=now)

class DebtTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.dummyAccount = NL_Account.objects.create(name='Dummy Bro', AccountNumber=1234067, owner = self.user)
        self.dummy = Contact.objects.create(first_name='Dummy', last_name='Man',
                                            object_id=999, owner = self.user, content_type= ContentType.objects.get(app_label='bankAccounts', model='nl_account'))

        self.normalDebt = Debt.objects.create(
            name= 'Normal Debt Amount',
            description= 'ranjawd jawdnwad awjdn',
            creditor= self.dummy,
            amount= 314.46,
            dueDate=now(),
            startDate=datetime.date(2019,10,3),
            owner = self.user
        )
        self.highDebt = Debt.objects.create(
            name= 'High Dept Amount',
            creditor= self.dummy,
            amount= 72018322.99,
            dueDate=now(),
            startDate=datetime.date(1997,10,3),
            owner = self.user
        )
        self.lowDebt = Debt.objects.create(
            name= 'Low Debt Amount',
            description= ' ijadjw wndijanwd awddjnaowia',
            creditor= self.dummy,
            amount= 0.01,
            dueDate=datetime.date(2021,1,18),
            startDate=now(),
            owner = self.user
        )
        self.negativeDebt = Debt.objects.create(
            name= 'Negative Debt Amount',
            creditor= self.dummy,
            amount= -124.12,
            dueDate=datetime.date(2030,12,1),
            startDate=datetime.date(1999,9,9),
            owner = self.user
        )

    def test_ordering(self):
        qs = Debt.objects.all()
        self.assertEqual(qs.count(), 4)
        self.assertEqual(qs[0].name, 'High Dept Amount')
        self.assertEqual(qs[1].name, 'Normal Debt Amount')
        self.assertEqual(qs[2].name, 'Low Debt Amount')
        self.assertEqual(qs[3].name, 'Negative Debt Amount')