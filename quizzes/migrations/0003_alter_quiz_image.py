# Generated by Django 4.2.6 on 2023-10-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_rename_user_answer_author_rename_user_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
