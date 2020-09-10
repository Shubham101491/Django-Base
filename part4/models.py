from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name