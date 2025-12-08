from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
    
@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
