# Generated by Django 5.0.4 on 2024-05-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=255, unique=True)),
                ('post_content', models.TextField(default='', max_length=1500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
    ]
