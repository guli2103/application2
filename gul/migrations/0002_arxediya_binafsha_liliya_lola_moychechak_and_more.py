# Generated by Django 4.1.3 on 2022-11-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arxediya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rangi', models.TextField()),
                ('soni', models.IntegerField(default=1)),
                ('narxi', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Binafsha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
                ('soni', models.IntegerField(default=1)),
                ('narxi', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Liliya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rangi', models.CharField(max_length=20)),
                ('soni', models.IntegerField(default=1)),
                ('narxi', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Lola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qayerdanligi', models.CharField(max_length=20)),
                ('rangi', models.CharField(max_length=20)),
                ('soni', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Moychechak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kattaligi', models.TextField()),
                ('soni', models.IntegerField(default=1)),
                ('narxi', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='atirgul',
            name='narxi',
            field=models.IntegerField(default=1),
        ),
    ]
