# Generated by Django 4.1.4 on 2022-12-08 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_alter_profile_options_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.profile', verbose_name='Профиль'),
        ),
    ]
