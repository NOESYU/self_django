from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hihi(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld() #model.py 에 있는 객체 새롭게 생성
        new_hello_world.text = temp
        new_hello_world.save() #디비에 저장

        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_world' : new_hello_world})

    elif request.method == 'GET':
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'Get Method'})