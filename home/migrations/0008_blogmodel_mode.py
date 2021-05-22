# Generated by Django 3.1.6 on 2021-05-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_blogmodel_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='mode',
            field=models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE')], max_length=10, null=True),
        ),
    ]
