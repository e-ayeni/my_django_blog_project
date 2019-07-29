from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from django import forms


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid()

    return render(request, 'users/register.html', {'form': form})
