# Generated by Django 3.1.5 on 2021-04-07 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
