# Generated by Django 3.1.6 on 2021-05-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blogmodel_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='mode',
        ),
    ]