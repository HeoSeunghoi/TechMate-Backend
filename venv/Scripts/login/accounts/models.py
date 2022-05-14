from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def createUser(self, email, username, password=None):
        if not email:
            raise ValueError('Must have user email')
        
        if not username:
            raise ValueError('Must have user username')
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.createUser(
            email,
            password = password,
            username = username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(default='',max_length = 100,null=False,blank = False,unique=True)
    email = models.EmailField(default='', max_length = 100, null = False, blank =False, unique=True)

    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin