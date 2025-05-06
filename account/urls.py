from django.urls import path
from . import views
from core.views import wallet_info

app_name = 'account'

urlpatterns = [
  path('register/', wallet_info, name='register'),
  path('login/', wallet_info, name='login'),
  path('profile/', wallet_info, name='profile'),
  path('logout/', wallet_info, name='logout'),
  path('deposit/', wallet_info, name='deposit'),
  path('spend/', wallet_info, name='spend'),
  path('transactions/', wallet_info, name='transactions'),
  path('change-password/', wallet_info, name='change_password'),

]