from rest_framework import serializers
from system import models


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'first_name', 'last_name', 'date_of_death']

