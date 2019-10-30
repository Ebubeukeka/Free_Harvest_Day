from __future__ import unicode_literals
from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
age_group = "Age Group"

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Please provide a first name"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Please provide a Last name"
        if not email_regex.match(postData['email']):
            errors["email"] = "Invalid email address"
        if not postData['password'] == postData['confirm_password']:
            errors["password"] = "Passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        if not email_regex.match(postData['login_email']):
            errors["login_email"] = "Invalid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    age_group = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class ContactManager(models.Manager):
    def contact_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["first_name"] = "Please provide a name"
        if not email_regex.match(postData['contact_email']):
            errors["email"] = "Invalid email address"
        return errors

class Contact(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContactManager()

class Staff(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    occupation = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
