from django.contrib import admin
from django.db import models
from django.db.models.fields import CharField


class UserContacts(models.Model):
    username = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    phonenumber = models.IntegerField()
    comments = models.TextField()

    def __str__(self) -> str:
        return self.username
