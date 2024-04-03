from django.contrib import admin
from .models import Company, Employee, Asset, CheckoutHistory

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(CheckoutHistory)
