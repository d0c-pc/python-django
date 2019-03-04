from django.shortcuts import render
from django.http import HttpResponse

def contato_view(request):
    return render(request, 'contato.html')