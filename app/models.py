from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.Many
	publication_date = models.DateTimeField()
	publisher = models.CharField(max_length=200)
	summary = models.CharField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	purchase_link = models.URLField()
	cover_image = models.URLField()
