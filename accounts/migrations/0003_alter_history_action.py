# Generated by Django 4.2.6 on 2023-10-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='action',
            field=models.CharField(choices=[('likes', 'likes'), ('quiz', 'quiz'), ('hint', 'hint'), ('create', 'create')], default='likes', max_length=20),
        ),
    ]
