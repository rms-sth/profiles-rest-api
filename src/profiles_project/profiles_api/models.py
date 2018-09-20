from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django to work with our custom user models """
    def create_user(self, email, name, password):
        """Creates a new profile object """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #makes lowercase all email inputs
        user = self.model(email=email, name=name)
        user.set_password(password) #encryptes password
        user.save(using=self._db)
        return  user

    def create_superuser(self, email, name, password):
        """Creates and save new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent "User Profiles" """
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"Used to get users' full name """
        return self.name

    def get_short_name(self):
        """Used to get users' short name """
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to string """
        return self.email
