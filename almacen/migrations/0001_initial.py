# Generated by Django 2.0.6 on 2018-10-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_api', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_programada', models.DateTimeField(blank=True, null=True)),
                ('fecha_hecho', models.DateTimeField(blank=True, null=True)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('picking', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.SmallIntegerField(default=0)),
                ('producto', models.CharField(blank=True, max_length=300, null=True)),
                ('de', models.CharField(blank=True, max_length=300, null=True)),
                ('para', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('compania', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
