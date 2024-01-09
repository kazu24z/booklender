from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    # -は含めない設計(ISBN-13)
    isbn = models.CharField(max_length=13)


class LenderBook(models.Model):
    lender = models.ForeignKey(
        User, related_name='lender', on_delete=models.CASCADE)
    borrower = models.ForeignKey(
        User, related_name='borrower', on_delete=models.CASCADE)
    name = models.ForeignKey(Book, related_name='name',
                             on_delete=models.CASCADE)
    lend_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
