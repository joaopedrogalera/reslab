# Generated by Django 2.2.2 on 2019-06-29 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResLabApp', '0006_laboratorio_adm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='adm',
        ),
    ]