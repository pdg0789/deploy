from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validation(self, form_data):
        errors = []

        #Check if inputs have data
        if len(form_data['name']) == 0:
            errors.append('Name is required')
        if len(form_data['username']) == 0:
            errors.append('Username is required')
        if len(form_data['password']) == 0:
            errors.append('Password is required')
        if len(form_data['password_confirmation']) == 0:
            errors.append('Password confirmation is required')

        #Check if username is duplicate
        user_record = User.objects.filter(username=form_data['username']).first()
        if user_record:
            errors.append('This username is already taken, please log in.')

        return errors

    def login_validation(self, form_data):
        errors = []

        #Check inputs have data
        if len(form_data['name']) < 3:
            errors.append('Name is required')
        if len(form_data['username']) < 3:
            errors.append('Username is required')
        if len(form_data['password']) < 8:
            errors.append('Password is required')

        user = User.objects.filter(username=form_data['username']).first()

        if user:
            password = str(form_data['password'])
            user_password = str(user.password)

            encryptedpw = bcrypt.hashpw(password, user_password)

            if encryptedpw == user_password:
                return user

            errors.append("Invalid password.")

        errors.append("That username has not be registered yet.")

        return errors

    def create_user(self, form_data):
        password = str(form_data['password'])
        encryptedpw = bcrypt.hashpw(password, bcrypt.gensalt())

        user = User.objects.create(
            name = form_data['name'],
            username = form_data['username'],
            password = encryptedpw
        )

        return user

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    trip = models.ManyToManyField("self", related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models. DateField()
    end_date = models.DateField()
    plan = models.TextField(max_length=400)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
