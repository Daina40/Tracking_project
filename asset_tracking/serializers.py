from rest_framework import serializers
from .models import Company, Employee, Asset, CheckoutHistory

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class CheckoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutHistory
        fields = '__all__'
