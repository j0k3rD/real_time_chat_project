from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            "admin1@admin1.com",
            password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user

# Users
class User(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length=50,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True,
                                    verbose_name="Active",
                                    help_text="lorem")
    staff = models.BooleanField(default=False,
                                   verbose_name="Staff status",
                                   help_text="lorem")
    admin = models.BooleanField(default=False,
                                       verbose_name="Admin status",
                                       help_text="lorem")

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, db):
        return True