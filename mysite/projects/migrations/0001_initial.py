# Generated by Django 3.2 on 2022-03-10 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
