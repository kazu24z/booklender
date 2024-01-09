from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    # -は含めない設計(ISBN-13)
    isbn = models.CharField(max_length=13)


class LenderRecord(models.Model):
    lender = models.ForeignKey(
        User, related_name='lenders', on_delete=models.CASCADE)
    borrower = models.ForeignKey(
        User, related_name='borrowers', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lend_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
