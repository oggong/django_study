from django.db import models


# Create your models here.
class book_title(models.Model):
    book_name = models.CharField(max_length=200)
    book_type = models.CharField(max_length=100)
    book_price = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name
