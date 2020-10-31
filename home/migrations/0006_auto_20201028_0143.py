# Generated by Django 3.1.1 on 2020-10-27 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_delete_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.RemoveField(
            model_name='art',
            name='likes',
        ),
        migrations.AddField(
            model_name='art',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
