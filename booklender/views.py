from django.contrib.auth.models import User
from booklender.models import Book, LenderRecord
from rest_framework import viewsets

from booklender.serializers import UserSerializer, BookSerializer, LenderRecordSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LenderRecordViewSet(viewsets.ModelViewSet):
    queryset = LenderRecord.objects.all()
    serializer_class = LenderRecordSerializer
