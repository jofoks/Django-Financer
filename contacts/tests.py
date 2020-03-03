from django.test import TestCase
from .models import Contact
from bankAccounts.models import NL_Account
from django.contrib.auth.models import User
import datetime
from django.contrib.contenttypes.models import ContentType


class ContactTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.cntct=Contact.objects.create(first_name='Dummy',
                                        last_name='Dude',
                                        email='Dummy@yeet.com',
                                        object_id=999,
                                        content_type= ContentType.objects.get(app_label='bankAccounts', model='nl_account'),
                                        owner= self.user)
