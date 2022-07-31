from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class JobPost(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=300, blank=False)