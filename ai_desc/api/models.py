from django.db import models

# Create your models here.
class Decriptions(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    user_req = models.TextField(max_length=1000)
    description_ru = models.TextField(max_length=1000, blank=True)
    error = models.TextField(max_length=255, blank=True)