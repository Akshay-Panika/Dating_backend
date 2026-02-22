from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_name   