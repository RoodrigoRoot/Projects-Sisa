# Generated by Django 3.0 on 2019-12-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AddField(
            model_name='projects',
            name='folio',
            field=models.IntegerField(default=1, verbose_name='Folio'),
            preserve_default=False,
        ),
    ]
