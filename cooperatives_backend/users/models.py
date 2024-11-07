from django.contrib.auth.models import AbstractUser
from django.db import models
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


length =255

class County(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name
auditlog.register(County)


class SubCounty(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name
auditlog.register(SubCounty)

class Ward(models.Model):
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name

auditlog.register(Ward)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# auditlog.register(CustomUserManager)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('national', 'National'),
        ('county', 'County'),        
        ('sp', 'Automation Service Provider'),
        ('fa', 'Funding Agency'),
        ('os', 'Other Stakeholders')
    )
    
  
    GEN_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('pnts', 'Prefer Not to Say'), 
    )
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    first_name =models.CharField(max_length=length, blank=True, null=True,)
    last_name = models.CharField(max_length=length, blank=True, null=True,)

    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = []  # Username field is not required anymore

    role = models.CharField(max_length=length, choices=ROLE_CHOICES, default="county")
    allias = models.CharField(max_length=length, blank=True, null=True,)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True,)
    position =  models.CharField(max_length=length, blank=True, null=True,)
    gender  = models.CharField(max_length=length, choices=GEN_CHOICES, blank=True, null=True,)
    yob =models.IntegerField(blank=True, null=True, default=1980)
    objects = CustomUserManager() 

    def __str__(self):
        return self.email
auditlog.register(CustomUser)