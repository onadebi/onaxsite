# Generated by Django 5.0.4 on 2024-04-25 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 21, 59, 9, 18572), verbose_name='date published'),
        ),
    ]