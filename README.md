# Ex02 Django ORM Web Application
## Date: 22/04/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](image.png)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Loan(models.Model):
    Customer_name=models.CharField(max_length=100)
    Mobile_no=models.IntegerField()
    Age=models.IntegerField()
    DoB=models.DateField()
    Loan_amount=models.IntegerField()
class LoanAdmin(admin.ModelAdmin):
    list_display=('Customer_name', 'Mobile_no', 'Age', 'DoB','Loan_amount')

admin.py
from django.contrib import admin
from .models import Loan,LoanAdmin
admin.site.register(Loan,LoanAdmin)
```


## OUTPUT
![alt text](PHOTO.png)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
