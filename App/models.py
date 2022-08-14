from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=12)
    desc=models.TextField()

    def __str__(self):
        return str((self.name,self.email))


class home(models.Model):
    
    email=models.CharField(max_length=12)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.email
        
class booking(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    From=models.CharField(max_length=20)
    to=models.CharField(max_length=20)

    def __str__(self):
        return str((self.firstname,self.lastname,self.email,self.From,self.to))
