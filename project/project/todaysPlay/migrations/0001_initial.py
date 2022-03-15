# Generated by Django 4.0.2 on 2022-03-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultureplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('placeName', models.CharField(max_length=50)),
                ('lineNumber', models.CharField(max_length=15)),
                ('station', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceNum', models.IntegerField()),
                ('Class', models.CharField(max_length=50)),
                ('PlaceName', models.CharField(max_length=50)),
                ('LineNumber', models.CharField(max_length=50)),
                ('Station', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('TelePhone', models.CharField(max_length=50)),
                ('Image', models.CharField(max_length=50)),
                ('Website', models.CharField(max_length=50)),
                ('OpeningHours', models.CharField(max_length=50)),
                ('Fee', models.CharField(max_length=50)),
                ('Closed', models.CharField(max_length=50)),
                ('PayFree', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProgramNumber', models.IntegerField()),
                ('Category', models.CharField(max_length=50)),
                ('ProgramName', models.CharField(max_length=50)),
                ('PlaceName', models.CharField(max_length=50)),
                ('Image', models.CharField(max_length=50)),
                ('StartDay', models.DateField()),
                ('EndDay', models.DateField()),
                ('TargetAudience', models.CharField(max_length=50)),
                ('Fee', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationName', models.CharField(max_length=30)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
                ('hosun', models.CharField(max_length=15)),
            ],
        ),
    ]
