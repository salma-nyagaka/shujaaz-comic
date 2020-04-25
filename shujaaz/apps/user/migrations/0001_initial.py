# Generated by Django 2.2.1 on 2020-04-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default='Regular User', max_length=256)),
                ('first_name', models.CharField(blank=True, max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('email', models.CharField(blank=True, max_length=256)),
            ],
        ),
    ]
