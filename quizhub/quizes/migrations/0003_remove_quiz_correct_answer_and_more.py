# Generated by Django 5.0.3 on 2024-10-04 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_alter_quiz_correct_answer'),
        ('users', '0002_remove_registeruser_password2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='number_of_questions',
        ),
        migrations.AddField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='users.registeruser'),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='quizes.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='users.registeruser')),
            ],
            options={
                'unique_together': {('quiz', 'user')},
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='winner_solution',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winning_quiz', to='quizes.solution'),
        ),
    ]
