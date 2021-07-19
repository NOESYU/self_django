from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hihi, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns = [
    path('hihi/', hihi, name='hi'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]