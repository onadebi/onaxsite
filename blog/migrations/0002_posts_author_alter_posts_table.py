# Generated by Django 5.0.4 on 2024-06-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='Onaefe', max_length=50),
        ),
        migrations.AlterModelTable(
            name='posts',
            table='Post',
        ),
    ]
