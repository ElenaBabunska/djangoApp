# Generated by Django 4.0.4 on 2022-07-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlowersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
