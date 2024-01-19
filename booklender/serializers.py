
from rest_framework import serializers
from django.contrib.auth.models import User

from booklender.models import Book, LenderRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'owner', 'title', 'author', 'isbn']


class LenderRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = LenderRecord
        fields = ['id', 'lender', 'borrower',
                  'book', 'lend_date', 'return_date']
