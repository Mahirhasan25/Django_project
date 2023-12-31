# Generated by Django 4.2.7 on 2023-11-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='INCOMPLETE', max_length=20)),
                ('catagory', models.CharField(choices=[('ACADEMIC', 'ACADEMIC'), ('JOB', 'JOB'), ('PERSONAL', 'PERSONAL')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('edit_cnt', models.IntegerField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
