from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hihi(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')
        return render(request, 'accountapp/hello_world.html',
                      context={'text': temp})
    elif request.method == 'GET':
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'Get Method'})