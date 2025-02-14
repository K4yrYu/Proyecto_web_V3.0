# Generated by Django 4.1.2 on 2024-06-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('consolas', models.CharField(max_length=100, verbose_name='Consolas')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('url_imagen', models.URLField(verbose_name='URL de la Imagen')),
            ],
        ),
    ]
