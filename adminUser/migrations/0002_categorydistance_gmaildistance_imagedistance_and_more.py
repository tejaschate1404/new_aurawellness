# Generated by Django 5.1.5 on 2025-02-05 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GmailDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DistanceHealing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('given_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=10)),
                ('born_date', models.DateField()),
                ('born_place', models.CharField(max_length=255)),
                ('born_country', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('position', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('division', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminUser.categorydistance')),
                ('gmail_addresses', models.ManyToManyField(blank=True, to='adminUser.gmaildistance')),
                ('images', models.ManyToManyField(blank=True, to='adminUser.imagedistance')),
                ('phone_numbers', models.ManyToManyField(blank=True, to='adminUser.phonedistance')),
            ],
        ),
        migrations.CreateModel(
            name='NotesDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='adminUser.distancehealing')),
            ],
        ),
    ]
