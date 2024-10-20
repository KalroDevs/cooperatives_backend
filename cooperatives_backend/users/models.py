from django.contrib.auth.models import AbstractUser
from django.db import models

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


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('national', 'National'),
        ('county', 'County'),        
        ('sp', 'Service Provider'),
        ('fa', 'Funding Agency'),
        ('os', 'Other Stakeholders')
    )
  
    GEN_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('pnts', 'Prefer Not to Say'), 
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = []  # Username field is not required anymore

    role = models.CharField(max_length=length, choices=ROLE_CHOICES, default="os")
    allias = models.CharField(max_length=length, blank=True, null=True,)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="counties", blank=True, null=True,)
    position =  models.CharField(max_length=length, blank=True, null=True,)
    gender  = models.CharField(max_length=length, choices=GEN_CHOICES, blank=True, null=True,)
    yob =models.IntegerField(blank=True, null=True, default=1980)

    def __str__(self):
        return self.username
