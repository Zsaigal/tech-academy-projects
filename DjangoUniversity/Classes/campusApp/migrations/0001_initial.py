# Generated by Django 5.0.2 on 2024-02-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_name', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=2)),
                ('Campus_Id', models.IntegerField(max_length=10)),
            ],
        ),
    ]
