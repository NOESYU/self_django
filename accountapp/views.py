from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hihi(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld() #model.py 에 있는 객체 새롭게 생성
        new_hello_world.text = temp
        new_hello_world.save() #디비에 저장

        return HttpResponseRedirect(reverse('accountapp:hi'))
        #urls.py에서 내가 지정해준 name

    elif request.method == 'GET':
        hello_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_list': hello_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hi')
    template_name ='accountapp/create.html'
