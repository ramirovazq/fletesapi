# Generated by Django 2.0.6 on 2018-10-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoalmacen',
            name='detalle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movimientoalmacen',
            name='propietario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
