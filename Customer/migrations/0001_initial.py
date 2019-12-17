# Generated by Django 3.0 on 2019-12-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bussines', models.CharField(max_length=15, verbose_name='Empresa')),
                ('representative', models.CharField(max_length=50, verbose_name='Encargado de Proyecto')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefono')),
            ],
        ),
    ]
