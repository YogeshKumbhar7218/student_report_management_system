# Generated by Django 4.0.4 on 2022-06-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticate',
            fields=[
                ('en_roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=20)),
                ('parent_user_name', models.CharField(max_length=20, null=True)),
                ('parent_passwd', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]