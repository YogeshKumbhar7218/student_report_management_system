# Generated by Django 4.0.4 on 2022-06-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_teacher_stack_student_activities_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_stack_student_activities',
            name='approved',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='teacher_stack_student_activities',
            name='points',
            field=models.IntegerField(null=True),
        ),
    ]
