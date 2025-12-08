from django.shortcuts import render
from .models import SubscriptionType

def subscription_list(request):
    # Беремо всі типи підписок з бази
    sub_types = SubscriptionType.objects.all()
    return render(request, 'subscriptions/list.html', {'sub_types': sub_types})