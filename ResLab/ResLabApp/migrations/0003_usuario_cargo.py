# Generated by Django 2.2.2 on 2019-06-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResLabApp', '0002_auto_20190626_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cargo',
            field=models.CharField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]