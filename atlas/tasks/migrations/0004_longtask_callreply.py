# Generated by Django 3.0.3 on 2020-05-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200513_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='longtask',
            name='callreply',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
