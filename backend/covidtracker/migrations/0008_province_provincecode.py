# Generated by Django 3.1.7 on 2021-07-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidtracker', '0007_auto_20210706_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='provinceCode',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]