from django.db import models

 
# Create your models here.
class Employee(models.Model):


    trade = models.CharField(max_length=100) 
    date = models.CharField(max_length=100)
    shares = models.CharField(max_length=100)
    symbols = models.CharField(max_length=100)
    buysell = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    age = models.CharField(max_length=100)


    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

   
    class Meta:  
        db_table = "tblemployee"


        
