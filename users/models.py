from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, user_name, user_email, user_password=None):
        if not user_email:
            raise ValueError("Users must have an email address")
        user = self.model(
            user_name=user_name,
            user_email=self.normalize_email(user_email)
        )
        user.set_password(user_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, user_email, user_password):
        user = self.create_user(user_name, user_email, user_password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_email

    @property
    def is_staff(self):
        return self.is_admin
