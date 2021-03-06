from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here. # UserManager는 슈퍼유저 생성할 때 호출됨 
class UserManager(BaseUserManager):
  
    # 일반 유저 생성 
    def create_user(self, username,password, **extra_fields):
        user = self.model(username = username,password=password)
        user.set_password(password)
        user.save()
        return user
        # try:
        #     user = self.model(username = username,  email = email,password=password)
        #     user.set_password(password)

        #     # extra_field.setdefault('is_staff', False)            
        #     # extra_field.setdefault('is_superuser', False)
        #     user.save()
        #     return user
        # except Exception as e:
        #     print(e)

    # 어드민 유저 생성 
    def create_superuser(self, username, password=None, **extra_fields):

        return self.create_user(username, password,**extra_fields)
        # try:
        #     superuser = self.create_user(username = username,password=password, email=email)
        #     superuser.set_password(password)
        #     superuser.is_admin = True            
        #     superuser.is_superuser = True            
        #     superuser.is_active = True           
        #     superuser.is_staff = True

        #     superuser.save()
        # except Exception as e:
        #     print(e)

class Member(AbstractBaseUser):
    last_login = None
    email = models.EmailField(max_length=100, null=True)
    username = models.CharField(max_length=20,unique=True)
    phone = models.CharField(max_length=12)

    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def has_perm(self, perm, obj=None):       
        return self.is_admin
    def has_module_perms(self, app_label):       
        return self.is_admin

    class Meta:
        db_table = "member"