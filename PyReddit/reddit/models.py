from time import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user

class Post(models.Model):
	Upvotes = models.IntegerField()
	Downvotes = models.IntegerField()
	Community = models.CharField(max_length=50)
	CreatedBy = models.ForeignKey(User, on_delete=models.SET(User.get_username))
	Title = models.CharField(max_length=150)
	BodyText = models.TextField()
	DateCreated = models.DateTimeField(default=timezone.now)
