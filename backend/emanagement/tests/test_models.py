from django.test import TestCase

from emanagement import models

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        models.BookPublish.objects.create(company_name="lol xD", website="https://github.com/shyamkumaryadav").genre.set([])
        # Set up non-modified objects used by all test methods
    
    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")

    def test_first_name_label(self):
        author = models.BookPublish.objects.first()
        field_label = author._meta.get_field('company_name').verbose_name
        self.assertEqual(field_label, 'company name')

    def test_date_of_death_label(self):
        author=models.BookPublish.objects.first()
        field_label = author._meta.get_field('website').verbose_name
        self.assertEqual(field_label, 'website')