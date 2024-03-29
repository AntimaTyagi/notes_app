# Generated by Django 3.2.7 on 2021-10-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_rename_signupform_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
