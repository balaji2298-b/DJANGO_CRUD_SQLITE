from django.db import models


class Men(models.Model):
	name = models.CharField(max_length=50)
	amount = models.CharField(max_length=10)
