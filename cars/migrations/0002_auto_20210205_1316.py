# Generated by Django 3.1.6 on 2021-02-05 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cars',
            unique_together={('car_make', 'model_name')},
        ),
    ]