from django.shortcuts import render

# Create your views here.
from .forms import UserRegistration

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html' ,{'new_user':new_user})
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


# responsible for registering a new user to our application and uses the UserRegistration class we created in our forms.py above as such if the form is valid, a new user is being created but the said user is not being saved directly into the database hence