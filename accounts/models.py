from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, student_num=0, phone=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, student_num=0, phone=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            name=name,
            student_num=student_num,
            phone=phone
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser
    
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    student_num = models.IntegerField()
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    phone = models.CharField(max_length=45)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_num', 'phone']

    class Meta:
        managed = True
        db_table = 'user'

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    @property
    def get_username(self):
        return self.username