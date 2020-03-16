from django.test import TestCase
from .csv_interpreter import handle_file
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from transaction.forms import CsvFileForm

class Handle_fileTestCase(TestCase):
    ''' python3 manage.py test static/scripts/tests.py '''
    def setUp(self):
        upload_file = open('transaction/cache/NL02INGB0751868809_01-01-2011_14-01-2020.csv', 'rb')
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}

        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.csvFile = CsvFileForm(file_dict)
    
    def test_functionality(self):
        self.assertTrue(handle_file(user=self.user, csv=self.csvFile , content_type='text/csv'))


