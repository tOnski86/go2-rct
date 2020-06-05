# Generated by Django 3.0.7 on 2020-06-05 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='date_updated',
            new_name='ts_updated',
        ),
        migrations.RemoveField(
            model_name='job',
            name='date_created',
        ),
        migrations.AddField(
            model_name='job',
            name='ts_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
