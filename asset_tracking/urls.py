from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetailAPIView.as_view(), name='company-detail'),
    path('employees/', views.EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employees-detail'),
    path('assets/', views.AssetListAPIView.as_view(), name='asset-list'),
    path('assets/<int:pk>/', views.AssetDetailAPIView.as_view(), name='assets-detail'),
    path('checkout-histories/', views.CheckoutHistoryListAPIView.as_view(), name='checkout-history-list'),
    path('checkout-histories/<int:pk>/', views.CheckoutHistoryDetailAPIView.as_view(), name='checkout-histories-detail'),
]
