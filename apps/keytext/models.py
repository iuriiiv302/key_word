from django.contrib.auth.models import User
from django.db import models


class KeyWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.TextField()
    full_text = models.TextField()


# class Key(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     key_word = models.TextField()
#
# class TextAll(models.Model):
#     key =models.ForeignKey(Key, on_delete=models.CASCADE)
#     full_EBSxt = models.TextField()