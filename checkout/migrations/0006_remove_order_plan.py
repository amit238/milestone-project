# Generated by Django 3.0.8 on 2020-07-31 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200731_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='plan',
        ),
    ]