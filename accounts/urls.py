from django.urls import path
from . import views

urlpatterns = [
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset/complete/', views.password_reset_complete, name='password_reset_complete'),
]
