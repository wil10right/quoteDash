from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def userValidator(self, postData):
        # print("POST_DATA",postData)
        errors = {}
        emailcheck = User.objects.all().values_list('email',flat=True)
        # print(emailcheck)
        # print(errors)
        if postData['reg'] == 'new':
            if len(postData['first'])<3:
                errors['first']="First name must have more than 3 characters."
            if len(postData['last'])<3:
                errors['last']="Last name must have more than 3 characters."
            if not EMAIL_REGEX.match(postData['email']):
                errors['email_wrong'] = "Please enter a valid email address"
            if postData['email'] in emailcheck:
                errors['email_taken'] = "That email is already registered"
            if len(postData['pw']) < 8:
                errors['passwrong']="Password MUST be equal to or longer than 8 characters"
            if postData['pw'] != postData['pc']:
                errors['passwrong']="Password confirmation fail"
            if errors:
                # print(errors)
                return errors
            else:
                hash = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
                makeme = User.objects.create(
                    first_name=postData['first'], 
                    last_name=postData['last'],
                    email=postData['email'],
                    password=hash
                    )
                return makeme

        if postData['reg'] == 'login':
            # filter always returns a list
            challenge = User.objects.filter(email=postData['email'])
            # print(challenge)
            if len(challenge):
                if bcrypt.checkpw(postData['pw'].encode(), challenge[0].password.encode()):
                    return challenge[0]
            return 'Invalid email & password combination'

    def quoteValidator(self, postData):
        errors = {}
        if len(postData['quote'])< 1:
            errors['quotelen']="Quote cannot be empty"
        if len(postData['author'])< 3:
            errors['authorlen']="Author name must be more than 3 characters"
        if errors:
            return errors
        else:
            return "go!"
    
    def editValidator(self, postData):
        errors = {}
        if len(postData['first']) > 1:
            errors['first_len']="Name cannot be left blank"
        if len(postData['last']) > 1:
            errors['last_len']="Name cannot be left blank"
        if len(postData['email']) > 1:
            errors['email_len']="Email cannot be left blank"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_wrong'] = "Please enter a valid email address"
        if errors:
            return errors
        else:
            return "go!"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, unique=True,)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} alias:{}>".format(self.first_name,self.last_name)

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="quotes")

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes")
    quote = models.ForeignKey(Quote, related_name="liked")
