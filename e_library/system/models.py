'''
System models of Book
'''
from django.db import models


class Book(models.Model):
    """
    system.models.Book Fields [id, first_name, last_name, date_of_death]
    """
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    date_of_death = models.DateField(
        verbose_name='Death Date', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
