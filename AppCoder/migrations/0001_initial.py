# Generated by Django 4.1.1 on 2022-10-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('edad', models.CharField(max_length=3)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
    ]
