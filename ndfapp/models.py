from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Avis(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    great = models.BooleanField(default=False)

    def __str__(self):
        return f"Avis de {self.name}"
