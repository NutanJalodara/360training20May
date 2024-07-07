from django.db import models

# Create your models here.

class p_name(models.Model):
    p_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.p_name}"

class p_id(models.Model):
    p_id = models.CharField(max_length=10,primary_key=True)

class p_contact(models.Model):
    p_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.p_contact}"

class p_address(models.Model):
    p_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.p_address}"
