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