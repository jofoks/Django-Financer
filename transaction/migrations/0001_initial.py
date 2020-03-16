# Generated by Django 3.0.3 on 2020-03-14 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=150)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('category', models.CharField(blank=True, max_length=150)),
                ('counterparty', models.CharField(blank=True, max_length=150)),
                ('account', models.CharField(blank=True, max_length=150)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-owner', '-date'],
            },
        ),
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='transaction/cache')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
