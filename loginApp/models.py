from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors["name"] = "Name should be atleast 2 characters long"
        if len(postData['alias']) < 2:
            errors["alias"] = "Alias should be atleast 2 characters long"
        if len(postData['email']) == 0:
            errors["email"] = "You must enter an email"

        elif not email_regex.match(postData['email']):
            errors["email"] = "Your email must be valid"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0 :
            errors["duplicate"] = "Email input is already in use"
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        
        return errors



class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=45)
    objects = UserManager()