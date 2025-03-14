# Generated by Django 5.0.3 on 2024-10-08 09:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solution',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions_list', to='quizes.quiz'),
        ),
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_solutions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quiz',
            name='solutions',
            field=models.ManyToManyField(blank=True, related_name='quizzes', to='quizes.solution'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='winner_solution',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winning_quiz', to='quizes.solution'),
        ),
        migrations.AlterUniqueTogether(
            name='solution',
            unique_together={('quiz', 'user')},
        ),
    ]
