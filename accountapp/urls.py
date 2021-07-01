from django.urls import path

from accountapp.views import hihi

app_name = 'accountapp'

urlpatterns = [
    path('hihi/', hihi, name='hi'),
]