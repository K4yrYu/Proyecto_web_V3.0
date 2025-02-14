# Generated by Django 4.1.2 on 2024-06-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megagames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('idconsola', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('url_imagen', models.URLField(verbose_name='URL de la Imagen')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio')),
            ],
        ),
    ]
