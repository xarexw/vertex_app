from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClientStat

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}

    # ЛОГІКА ДЛЯ КЛІЄНТА
    if not user.is_staff:
        # статистика (вага/зріст)
        stat, created = ClientStat.objects.get_or_create(user=user)
        
        # останні тренування
        recent_records = user.training_records.all().order_by('-created_at')[:5]
        
        context['stat'] = stat
        context['recent_records'] = recent_records
        
    # ЛОГІКА ДЛЯ ТРЕНЕРА
    else:
        #  сертифікати
        certificates = user.certificates.all().order_by('-date_issued')
        
        context['certificates'] = certificates

    return render(request, 'users/profile.html', context)