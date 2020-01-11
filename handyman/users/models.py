from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    CHOICES = (
        ('Client', 'Client'),
        ('Company', 'Company'),
    )

    status = models.CharField(max_length=7, choices=CHOICES, help_text='Please specify if you register as Client or Company')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.status
