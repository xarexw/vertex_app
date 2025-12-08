from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # після реєстрації - вхід
    template_name = 'registration/signup.html'
    
@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
