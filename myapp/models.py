from django.db import models

class Students(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profilePic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Added profile picture field

    def __str__(self):
        return self.firstName

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


