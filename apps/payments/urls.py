from django.urls import path
from .views import create_order, mock_payment

urlpatterns = [
    # cтворення замовлення (приймає ID підписки)
    path('create/<int:sub_id>/', create_order, name='create_order'),
    
    # cторінка банку (приймає ID замовлення)
    path('gateway/<int:order_id>/', mock_payment, name='mock_payment'),
]