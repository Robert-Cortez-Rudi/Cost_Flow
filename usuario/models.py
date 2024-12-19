from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}"
# APRIMORAR 