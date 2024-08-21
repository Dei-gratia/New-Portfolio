# Generated by Django 5.1 on 2024-08-16 08:16

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
import portfolio.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('profile_img', models.ImageField(upload_to='profile/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('greeting', models.CharField(max_length=20)),
                ('career', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('picture', models.ImageField(upload_to='home/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField()),
                ('future_scope', models.TextField(blank=True)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=254)),
                ('role', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('primary', models.BooleanField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.about')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('primary', models.BooleanField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.about')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=254)),
                ('social_icon', models.CharField(blank=True, max_length=100)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.about')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=254)),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='portfolio.projects')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=254)),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='portfolio.projects')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('order', portfolio.fields.OrderField(blank=True, default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='portfolio.category')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
