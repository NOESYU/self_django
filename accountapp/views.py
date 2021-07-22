from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForms
from accountapp.models import HelloWorld


@login_required(login_url=reverse_lazy('accountapp:login'))
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

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(login_required(login_url=reverse_lazy('accountapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('accountapp:login')), 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForms
    success_url = reverse_lazy('accountapp:hi')
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

@method_decorator(login_required(login_url=reverse_lazy('accountapp:login')), 'get')
@method_decorator(login_required(login_url=reverse_lazy('accountapp:login')), 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/delete.html'
