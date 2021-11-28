# Generated by Django 2.1.4 on 2021-11-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_serial', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('style', models.CharField(max_length=10)),
                ('details', models.TextField(max_length=1000000)),
            ],
        ),
    ]
