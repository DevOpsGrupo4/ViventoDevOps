# Generated by Django 3.2.3 on 2022-11-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0004_alter_empleado_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.CharField(max_length=250, null=True, verbose_name='Cargo'),
        ),
    ]