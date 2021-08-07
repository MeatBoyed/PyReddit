from django.shortcuts import render
from .models import Post

# Create your views here.
def homePage(request):
	context = {
		"title": "Home",
		"Posts": Post.objects.all()
	}
	print(request.user.is_authenticated)
	return render(request, "reddit/homePage.html", context=context)