from django.shortcuts import render,redirect
from .CustomForms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def registerPage(request):

	if request.method == "POST":
		form = UserRegistrationForm(request.POST)	
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f"Account created for {username}. Please Login")
			return redirect("user-login")
	else:
		form = UserRegistrationForm()

	context = {
		"title": "Create Account",
		"form": form
	}
	
	return render(request, "users/registerPage.html", context)


def profilePage(request):

	return render(request, "users/profilePage.html")