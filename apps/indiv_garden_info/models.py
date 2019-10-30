from __future__ import unicode_literals
from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Please provide a first name"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Please provide a Last name"
        if not email_regex.match(postData['email']):
            errors["email"] = "invalid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Garden(models.Model):
    garden_name = models.CharField(max_length=45)
    garden_address = models.CharField(max_length=45)
    ward_num = models.IntegerField()
    plant_date = models.DateTimeField()
    plans = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
