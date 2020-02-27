from django.test import TestCase
from .models import Contact
from bankAccounts.models import NL_Account
import datetime
from django.contrib.contenttypes.models import ContentType


class ContactTestCase(TestCase):
    def setUp(self):
        self.cntct=Contact.objects.create(first_name='Dummy',
                                        last_name='Dude',
                                        email='Dummy@yeet.com',
                                        object_id=999,
                                        content_type= ContentType.objects.get(app_label='bankAccounts', model='nl_account'))
