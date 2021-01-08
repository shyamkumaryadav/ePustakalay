"""
TEST for management appps.
"""
from django.test import TestCase
from emanagement.models import Book


class FTest(TestCase):
    '''
    Test: FTest
    For: Time Pass
    '''
    def setUp(self):
        pass    

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)