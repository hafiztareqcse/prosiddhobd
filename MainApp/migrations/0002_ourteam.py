# Generated by Django 3.2.2 on 2021-05-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('image', models.ImageField(upload_to='our_team')),
                ('facebook', models.CharField(blank=True, max_length=264)),
                ('twitter', models.CharField(blank=True, max_length=264)),
                ('instagram', models.CharField(blank=True, max_length=264)),
                ('linkedin', models.CharField(blank=True, max_length=264)),
            ],
        ),
    ]