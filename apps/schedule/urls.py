from django.urls import path
from .views import schedule_list, session_manage, add_record, session_summary

urlpatterns = [
    path('', schedule_list, name='schedule'),
    path('manage/<int:session_id>/', session_manage, name='session_manage'),
    path('manage/<int:session_id>/add/', add_record, name='add_record'),
    path('manage/<int:session_id>/summary/', session_summary, name='session_summary'),
]