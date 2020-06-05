# Generated by Django 3.0.7 on 2020-06-05 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('job_status', models.CharField(choices=[('DR', 'Draft'), ('PU', 'Published'), ('CL', 'Closed')], default='DR', max_length=2)),
                ('employment_type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Pull Time')], default='FT', max_length=2)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
