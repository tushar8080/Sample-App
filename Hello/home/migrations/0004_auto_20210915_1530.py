# Generated by Django 3.2.6 on 2021-09-15 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=122),
        ),
    ]
