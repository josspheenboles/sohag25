# Generated by Django 4.1 on 2025-03-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
