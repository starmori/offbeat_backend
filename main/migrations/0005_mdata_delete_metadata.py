# Generated by Django 4.0.8 on 2022-11-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenid', models.IntegerField()),
                ('metadata', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Metadata',
        ),
    ]
