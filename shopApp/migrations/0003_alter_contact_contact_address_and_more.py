# Generated by Django 4.1 on 2025-03-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(max_length=30),
        ),
    ]
