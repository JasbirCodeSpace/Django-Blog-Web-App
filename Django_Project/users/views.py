from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(requsest):
	if requsest.method == "POST":
		form = UserRegistrationForm(requsest.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(requsest,f'Account created for {username}!')
			return redirect('blog-home')

	else:
		form = UserRegistrationForm()
	return render(requsest,'users/register.html',{'form':form})
