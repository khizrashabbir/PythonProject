from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Cars(models.Model):
    registration_no = models.CharField(max_length=100)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

# color, model, make, registration no,
