from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        # create an empty register form
        form = UserCreationForm()
    else:
        # processing of the fully form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # performing log in and return to homepage
            login(request, new_user)
            return redirect('learning_logs:index')
    # displays an empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

