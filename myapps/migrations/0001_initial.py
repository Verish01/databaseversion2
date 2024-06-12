# Generated by Django 5.0.6 on 2024-05-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventorydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('quantity', models.TextField()),
                ('supplier', models.CharField(max_length=30)),
                ('photos', models.ImageField(upload_to='Inventph/')),
            ],
        ),
    ]
