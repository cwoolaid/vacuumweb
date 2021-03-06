# Generated by Django 4.0.2 on 2022-02-20 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a vacuum type (ex. cordless, robot etc.)', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the model name', max_length=20)),
                ('description', models.CharField(help_text='Product name/description appeared on website', max_length=200)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacuums.brand')),
                ('type', models.ManyToManyField(help_text='Select a vacuum type for this model', to='vacuums.Type')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Enter the 4-digit inventory number', max_length=4)),
                ('date_received', models.DateField(blank=True, null=True, verbose_name='Received')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacuums.model')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacuums.country'),
        ),
    ]
