# Generated by Django 4.2.5 on 2023-10-02 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_choice_votes_question_choice_delete_questionchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice',
            field=models.ManyToManyField(related_name='choice', to='polls.choice'),
        ),
    ]
