# Generated by Django 2.2.2 on 2019-06-29 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResLabApp', '0004_auto_20190629_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('sigla', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=2)),
                ('inicio', models.CharField(max_length=5)),
                ('fim', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('sala', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nroComp', models.IntegerField()),
                ('dpto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResLabApp.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('versao', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('nome', 'versao')},
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('estado', models.CharField(max_length=1)),
                ('horarios', models.ManyToManyField(to='ResLabApp.Horario')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResLabApp.Laboratorio')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResLabApp.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='softwares',
            field=models.ManyToManyField(to='ResLabApp.Software'),
        ),
    ]