from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html', {"name": "kbroms app"});
def forms(request):
    return render(request, 'customs/forms.html', {});