# Generated by Django 2.2.7 on 2019-12-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_auto_20191129_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='entrada',
            field=models.DateField(auto_now=True),
        ),
    ]