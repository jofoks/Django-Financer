# Generated by Django 3.0.3 on 2020-03-03 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='US_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routingNumber', models.IntegerField(verbose_name='Routing Number')),
                ('accountNumber', models.IntegerField(unique=True, verbose_name='Account Number')),
                ('accountType', models.CharField(choices=[('checkings', 'Checkings'), ('savings', 'Savings')], max_length=50, verbose_name='Account Type')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'US Bank Account',
            },
        ),
        migrations.CreateModel(
            name='NL_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('AccountNumber', models.CharField(max_length=34, unique=True, verbose_name='Account Number')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'NL Bank Account',
            },
        ),
    ]
