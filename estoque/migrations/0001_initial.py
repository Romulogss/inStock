# Generated by Django 2.2.7 on 2019-11-29 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('descricao', models.CharField(max_length=150)),
                ('fabricacao', models.DateField()),
                ('validade', models.DateField()),
                ('unidades', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produtos', to='estoque.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fabricacao', models.DateField()),
                ('validade', models.DateField()),
                ('entrada', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lotes', to='estoque.Produto')),
            ],
        ),
    ]
