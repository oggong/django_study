from django.db import models

from django.db.models.deletion import CASCADE,SET_DEFAULT,SET_NULL

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200,null=False)
    user_id = models.CharField(max_length=200,null=False,primary_key=True)
    user_password = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.user_name

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    writer_id = models.ForeignKey(User, on_delete=SET_DEFAULT,default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content