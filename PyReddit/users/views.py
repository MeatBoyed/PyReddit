from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registerPage(request):

	if request.method == "POST":
		form = UserCreationForm(request.POST)	
		if form.is_valid():
			username = form.cleaned_data.get("username")
			messages.success(request, f"Account created for {username}. Please Login")
			return redirect("user-login")
	else:
		form = UserCreationForm()

	context = {
		"title": "Create Account",
		"form": form
	}
	
	return render(request, "users/registerPage.html", context)

def loginPage(request):
	return render(request, "users/loginPage.html")