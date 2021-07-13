from django.urls import path

from accountapp.views import hihi, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hihi/', hihi, name='hi'),
    path('create/', AccountCreateView.as_view(), name='create')
]