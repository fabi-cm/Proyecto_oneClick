# Generated by Django 4.2.1 on 2023-05-07 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='user/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Biografia')),
                ('telf', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['id'],
            },
        ),
    ]
