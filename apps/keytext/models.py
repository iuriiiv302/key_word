from django.db import models


class KeyWord(models.Model):
    key = models.TextField()
    full_text = models.TextField()
