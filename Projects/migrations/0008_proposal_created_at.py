# Generated by Django 3.0 on 2020-01-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0007_auto_20200103_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
