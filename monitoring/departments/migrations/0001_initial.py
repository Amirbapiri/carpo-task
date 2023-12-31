# Generated by Django 4.0.7 on 2023-11-15 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='hosts.host')),
            ],
        ),
    ]
