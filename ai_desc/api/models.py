from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    date_registration = models.DateTimeField(auto_now_add=True)
    if_sub = models.BooleanField(default=False)
    email = models.EmailField(max_length=250)
    tokens = models.IntegerField(default=0)

class Decriptions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    request_id = models.AutoField(primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    user_req = models.TextField(max_length=1000)
    description_ru = models.TextField(max_length=1000, blank=True)
    error = models.TextField(max_length=255, blank=True)