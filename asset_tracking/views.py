from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Employee, Asset, CheckoutHistory
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    AssetSerializer,
    CheckoutHistorySerializer,
)


class ObjectRetrieveMixin:
    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(APIView, ObjectRetrieveMixin):
    def get(self, request, pk):
        company = self.get_object(Company, pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def patch(self, request, pk):
        company = self.get_object(Company, pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(Company, pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeListAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailAPIView(APIView, ObjectRetrieveMixin):
    def get(self, request, pk):
        employee = self.get_object(Employee, pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = self.get_object(Employee, pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employee = self.get_object(Employee, pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(Employee, pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssetListAPIView(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDetailAPIView(APIView, ObjectRetrieveMixin):
    def get(self, request, pk):
        asset = self.get_object(Asset, pk)
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    def patch(self, request, pk):
        asset = self.get_object(Asset, pk)
        serializer = AssetSerializer(asset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        asset = self.get_object(Asset, pk)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckoutHistoryListAPIView(APIView):
    def get(self, request):
        checkout_histories = CheckoutHistory.objects.all()
        serializer = CheckoutHistorySerializer(checkout_histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CheckoutHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CheckoutHistoryDetailAPIView(APIView, ObjectRetrieveMixin):
    def get(self, request, pk):
        checkout_history = self.get_object(CheckoutHistory, pk)
        serializer = CheckoutHistorySerializer(checkout_history)
        return Response(serializer.data)
    
    def put(self, request, pk):
        checkout_history = self.get_object(CheckoutHistory, pk)
        serializer = CheckoutHistorySerializer(checkout_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        checkout_history = self.get_object(CheckoutHistory, pk)
        serializer = CheckoutHistorySerializer(checkout_history, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checkout_history = self.get_object(CheckoutHistory, pk)
        checkout_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
