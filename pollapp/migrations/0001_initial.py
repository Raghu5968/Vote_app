# Generated by Django 4.2.6 on 2024-01-22 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidatename', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('partyname', models.CharField(max_length=200, null=True)),
                ('candidate_pic', models.ImageField(blank=True, default='pic.png', null=True, upload_to='')),
                ('partysymbol', models.ImageField(blank=True, default='pic.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=100)),
                ('voterage', models.IntegerField(null=True)),
                ('profile_pic', models.ImageField(blank=True, default='pic.png', null=True, upload_to='')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pollapp.category')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foodappusers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollapp.candidate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollapp.voter')),
            ],
        ),
    ]
