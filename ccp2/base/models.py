from django.db import models

# Create your models here.

class ContactForm(models.Model): 
    from_email = models.EmailField(max_length=10)
    subject = models.CharField(max_length=10)
    message = models.CharField(max_length=10)