# Generated by Django 4.2.1 on 2023-05-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='contacto_tipo',
            field=models.IntegerField(choices=[[0, 'Pedir informacion'], [1, 'Mandar una queja'], [3, 'Sugerir, recomendar']], default=[0, 'Pedir informacion'], verbose_name='Tipo de Contacto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='subscripcion',
            field=models.BooleanField(default=False, verbose_name='Recibir correos de productos e informacion'),
        ),
    ]
