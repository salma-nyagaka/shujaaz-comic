# Generated by Django 2.2.1 on 2020-04-26 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0002_delete_characters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comic.Comic')),
            ],
        ),
    ]
