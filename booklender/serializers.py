
from rest_framework import serializers
from django.contrib.auth.models import User

from booklender.models import Book, LenderRecord


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['url', 'title', 'author', 'isbn']


class LenderRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LenderRecord
        fields = ['url', 'lender', 'borrower',
                  'book', 'lend_date', 'return_date']
