from django.db import models

from .validators import validate_amazing

class Product(models.Model):
    title = models.CharField(
        null=False, blank=False, max_length=25, validators=[validate_amazing]
        )
    slug = models.CharField(unique=True, max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title