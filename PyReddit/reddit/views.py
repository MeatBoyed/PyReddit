from django.shortcuts import render
from .models import Post

# Create your views here.
def homePage(request):
	context = {
		"Posts": Post.objects.all()
	}
	return render(request, "reddit/homePage.html", context=context)