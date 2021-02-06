# Generated by Django 3.1.6 on 2021-02-06 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=136)),
            ],
            options={
                'ordering': ('car_make', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=72)),
            ],
            options={
                'ordering': ('make',),
            },
        ),
        migrations.CreateModel(
            name='CarRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField()),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='cars.carmodels')),
            ],
        ),
        migrations.AddField(
            model_name='carmodels',
            name='car_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.cars'),
        ),
        migrations.AlterUniqueTogether(
            name='carmodels',
            unique_together={('name', 'car_make')},
        ),
    ]
