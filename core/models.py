from django.db import models
from multiselectfield import MultiSelectField

Choices = (('HTML',"HTML"),
            ('Python',"PYTHON"),
            ('Django',"DJANGO"),
            ('Javascript',"Js"),
            ('SQL',"Mysql"),
    )   

# Create your models here.
# About Model
class About(models.Model):
    name = models.CharField(max_length=100,verbose_name="Enter Your Name")
    profile = models.CharField(max_length=100,verbose_name="Enter Your Profile")
    email = models.EmailField(max_length=100,unique=True,verbose_name="Enter Your E-mail")
    phone = models.CharField(max_length=15,unique=True,verbose_name="Enter Your Phone")
    description = models.TextField(max_length=600,verbose_name="About You ")
    image = models.ImageField(upload_to="about",verbose_name="Upload Image")
    skill = MultiSelectField(choices=Choices,verbose_name="Skills ")

   #  db_table = "about"

# Service Model
class Service(models.Model):
    title = models.CharField(max_length=100,verbose_name="Service Title")
    description = models.TextField(max_length=600,verbose_name="Service Description")

    #class Meta:
   #     db_table = "service"

# Work Model
class Work(models.Model):
    title = models.CharField(max_length=100,verbose_name="Work Title")
    image = models.ImageField(upload_to="work",verbose_name="Upload Image")
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=600,verbose_name="Work Description")

   # class Meta:
    #    db_table = "work"
#Blog Model

