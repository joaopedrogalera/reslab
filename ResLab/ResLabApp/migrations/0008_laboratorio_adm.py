# Generated by Django 2.2.2 on 2019-06-29 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResLabApp', '0007_remove_laboratorio_adm'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='adm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ResLabApp.Usuario'),
            preserve_default=False,
        ),
    ]
