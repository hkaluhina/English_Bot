# Generated by Django 4.1.4 on 2022-12-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(verbose_name='ID user in social network')),
                ('name', models.TextField(verbose_name='Name of the user')),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
    ]
