from django.test import TestCase
from .models import KeyWord, Category
from django.contrib.auth.models import User

class KeyWordTestCase(TestCase):
    def setUp(self):
        self.one = KeyWord.objects.create(name=  'a kywrd: 1' )
        self.two = KeyWord.objects.create(name=  'd kywrd: 2' )
        self.three = KeyWord.objects.create(name='b kywrd: 3' )
        self.four = KeyWord.objects.create(name= 'e kywrd: 4' )
        self.five = KeyWord.objects.create(name= 'c kywrd: 5' )

    def test_ordering(self):
        qs = KeyWord.objects.all()
        self.assertEqual(qs.count(), 5)
        self.assertEqual(qs[0].name, 'a kywrd: 1' )
        self.assertEqual(qs[1].name, 'b kywrd: 3' )
        self.assertEqual(qs[2].name, 'c kywrd: 5' )
        self.assertEqual(qs[3].name, 'd kywrd: 2' )
        self.assertEqual(qs[4].name, 'e kywrd: 4' )

class CategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.kw_one = KeyWord.objects.create(name= 'kywrd: 1' )
        self.kw_two = KeyWord.objects.create(name= 'kywrd: 2' )
        self.kw_three = KeyWord.objects.create(name= 'kywrd: 3' )
        self.kw_four = KeyWord.objects.create(name= 'kywrd: 4' )
        self.kw_five = KeyWord.objects.create(name= 'kywrd: 5' )

        self.single = Category.objects.create(name= 'B Dummt', owner = self.user )
        self.single.keywords.add(self.kw_three)
        self.double = Category.objects.create(name= 'C Dummt', owner = self.user )
        self.double.keywords.add(self.kw_three)
        self.double.keywords.add(self.kw_four)
        self.many = Category.objects.create(name= 'A Dummy', owner = self.user )
        self.many.keywords.add(self.kw_one)
        self.many.keywords.add(self.kw_two)
        self.many.keywords.add(self.kw_three)
        self.many.keywords.add(self.kw_four)
        self.many.keywords.add(self.kw_five)

    def test_ordering(self):
        qs = Category.objects.all()
        self.assertEqual(qs.count(), 3)
        self.assertEqual(qs[0].name, 'A Dummy' )
        self.assertEqual(qs[1].name, 'B Dummt' )
        self.assertEqual(qs[2].name, 'C Dummt' )