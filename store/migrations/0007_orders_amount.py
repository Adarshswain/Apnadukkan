# Generated by Django 3.1.1 on 2020-10-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
