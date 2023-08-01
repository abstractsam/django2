# Generated by Django 4.2.3 on 2023-08-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=1)),
                ('cartype', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=1)),
            ],
        ),
    ]