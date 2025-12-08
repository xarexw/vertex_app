from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import uuid

from subscriptions.models import SubscriptionType
from .models import Order, Transaction

@login_required
def create_order(request, sub_id):
    # знаходження товар (абонемент)
    sub_type = get_object_or_404(SubscriptionType, id=sub_id)
    
    # створення Ордеру (Чернетка)
    order = Order.objects.create(
        user=request.user,
        subscription_type=sub_type,
        amount=sub_type.price,
        status='new'
    )
    
    # створення транзакції (Очікування)
    # генеруємо фейковий ID транзакції, як це робить банк
    trx_id = f"TRX-{uuid.uuid4().hex[:10].upper()}"
    
    Transaction.objects.create(
        order=order,
        transaction_id=trx_id,
        amount=order.amount,
        status='pending'
    )
    
    # перекидаємо клієнта на сторінку оплати (Mock Bank)
    return redirect('mock_payment', order_id=order.id)

@login_required
def mock_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'payments/mock_gateway.html', {'order': order})
