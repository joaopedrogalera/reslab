# Generated by Django 2.2.2 on 2019-06-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResLabApp', '0008_laboratorio_adm'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='diasemana',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data',
            field=models.DateField(blank=True),
        ),
    ]
