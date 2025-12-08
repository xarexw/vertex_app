from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ClientStat
    
@login_required
def profile_view(request):
    stat, created = ClientStat.objects.get_or_create(user=request.user)
    
    # отримання останніх 5 записів тренувань
    # 'training_records' - related_name, прописане в apps/schedule/models.py
    recent_records = request.user.training_records.all().order_by('-created_at')[:5]
    
    context = {
        'user': request.user,
        'stat': stat,
        'recent_records': recent_records
    }
    
    return render(request, 'users/profile.html', context)
    # return render(request, 'users/profile.html', {'user': request.user})
