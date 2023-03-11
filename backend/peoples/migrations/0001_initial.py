# Generated by Django 4.1.2 on 2022-10-28 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('role', models.CharField(choices=[('cl', 'Collector'), ('bw', 'Branch Owner')], default='bw', max_length=5)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.branch')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.branch')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peoples.staff')),
            ],
            options={
                'unique_together': {('name', 'branch')},
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=11)),
                ('nid_number', models.CharField(blank=True, max_length=25, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('serial_number', models.IntegerField(default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.branch')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peoples.team')),
            ],
        ),
    ]
