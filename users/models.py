from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField('Email address')
    phone_number = models.CharField(max_length=20)
    birthday_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname, self.lastname
