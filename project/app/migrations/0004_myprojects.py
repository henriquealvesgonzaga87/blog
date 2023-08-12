# Generated by Django 4.2.3 on 2023-08-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mystudies_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('readme', models.URLField()),
                ('resume', models.TextField()),
            ],
            options={
                'db_table': 'myprojects',
            },
        ),
    ]
