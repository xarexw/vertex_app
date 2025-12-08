from django.urls import path
from .views import SignUpView

urlpatterns = [
    # cторінка реєстрації (http://127.0.0.1:8000/accounts/signup/)
    path('signup/', SignUpView.as_view(), name='register'),
]