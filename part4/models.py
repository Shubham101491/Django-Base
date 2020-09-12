from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name