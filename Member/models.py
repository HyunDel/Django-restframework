from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    # 일반 유저 생성 
    def create_user(self, username, email=None, password = None, **extra_field):
        try:
            user = self.model(username = username,  email = email)

            extra_field.setdefault('is_staff', False)            
            extra_field.setdefault('is_superuser', False)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)

    # 어드민 유저 생성 
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        try:
            superuser = self.create_user(username = username,password=password, email=email)
            superuser.set_password(password)
            superuser.is_admin = True            
            superuser.is_superuser = True            
            superuser.is_active = True           
            superuser.is_staff = True

            superuser.save()
        except Exception as e:
            print(e)

class User(AbstractBaseUser):

    email = models.EmailField(max_length=100, null=True)
    username = models.CharField(max_length=20,unique=True)
    phone = models.CharField(max_length=12)
    
    is_staff = models.BooleanField(default=False)    
    is_admin = models.BooleanField(default=False)    
    is_active = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def has_perm(self, perm, obj=None):       
        return self.is_admin
    def has_module_perms(self, app_label):       
        return self.is_admin

    class Meta:
        db_table = "User"