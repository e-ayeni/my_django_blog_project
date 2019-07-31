from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from django import forms


def register(request):
    if request.method == 'POST':
        # if the request method (from the template) is post, then create the User

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks/')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
