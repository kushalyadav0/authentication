# Generated by Django 5.1.7 on 2025-03-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
