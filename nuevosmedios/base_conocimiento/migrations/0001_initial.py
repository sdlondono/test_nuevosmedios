# Generated by Django 3.0.7 on 2020-06-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('arma', models.CharField(max_length=50)),
                ('arma_dps', models.IntegerField()),
                ('arma_type', models.CharField(max_length=50)),
            ],
        ),
    ]