from django.db import models
# the default import for modifying the default user schema/table provided by django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        #  to normalize the email, means that second phrase of email is case insensitive
        email =self.normalize_email(email)
        # create a user object with email and name instead of its default. Ex. username, email
        user=self.model(email=email,name=name)
        #  to enable django to encrypt the password inputted so that it will be secure.
        user.set_password(password)
        #  save this user object with the Database defined
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given user object"""
        user=self.create_user(email,name,password)
        #  set some of the property to true so that it becomes a proper admin
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user




class userprofile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELD= ['name']

    def get_fullname(self):
        """retrieve full name"""
        return self.name

    def get_shortname(self):
        """retrieve short name"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email


# Create your models here.
