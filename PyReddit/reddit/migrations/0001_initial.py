# Generated by Django 3.2.5 on 2021-08-06 08:08

from django.conf import settings
import django.contrib.auth.base_user
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Upvotes', models.IntegerField()),
                ('Downvotes', models.IntegerField()),
                ('Community', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=150)),
                ('BodyText', models.TextField()),
                ('DateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('CreatedBy', models.ForeignKey(on_delete=models.SET(django.contrib.auth.base_user.AbstractBaseUser.get_username), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
