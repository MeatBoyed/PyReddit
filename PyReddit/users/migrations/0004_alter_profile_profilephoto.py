# Generated by Django 3.2.5 on 2021-08-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_profiles_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePhoto',
            field=models.ImageField(default='default.jpeg', upload_to='profilePhotos'),
        ),
    ]
