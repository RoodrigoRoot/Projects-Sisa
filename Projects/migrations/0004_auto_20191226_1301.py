# Generated by Django 3.0 on 2019-12-26 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20191218_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['created_at'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
    ]
