# Generated by Django 3.1.2 on 2020-10-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_auto_20201022_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Hotel')),
                ('address', models.CharField(max_length=50, verbose_name='Dirección')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Zona_Turistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la Zona Turistica')),
                ('address', models.CharField(max_length=50, verbose_name='Dirección')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
            ],
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre del Restaurante'),
        ),
    ]
