from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'