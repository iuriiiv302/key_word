from django.contrib.auth.models import User
from django.db import models


class KeyWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.TextField()
    full_text = models.TextField()


