# Generated by Django 3.0.3 on 2020-05-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_longtask_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longtask',
            old_name='status',
            new_name='risposta',
        ),
    ]
