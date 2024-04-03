from django.db import models
from django.utils import timezone

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee_name

class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    def __str__(self):
        return self.asset_name

class CheckoutHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100, blank=True)
    
    def formatted_checkout_date(self):
        return self.checkout_date.strftime('%d-%b-%Y, %I:%M %p %A')
    
    def formatted_return_date(self):
        if self.return_date:
            return self.return_date.strftime('%d-%b-%Y, %I:%M %p %A')
        else:
            return "Not Returned Yet"
    
    def __str__(self):
        return f"{self.asset} - {self.employee} - {self.checkout_date}"

