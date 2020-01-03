# Generated by Django 3.0 on 2020-01-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_auto_20191226_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='justification',
            field=models.TextField(default=1, verbose_name='Justificación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='limitations',
            field=models.TextField(default=1, verbose_name='Limitaciones'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='requirements',
            field=models.TextField(default=1, verbose_name='Requerimientos '),
            preserve_default=False,
        ),
    ]