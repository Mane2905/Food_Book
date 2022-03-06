# Generated by Django 3.2.7 on 2022-03-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20220303_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField()),
                ('address_1', models.TextField()),
                ('address_2', models.TextField(default='')),
                ('city', models.TextField()),
                ('pin', models.TextField()),
                ('phone', models.TextField()),
            ],
        ),
    ]