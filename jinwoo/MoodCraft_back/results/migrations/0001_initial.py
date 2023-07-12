# Generated by Django 4.2.3 on 2023-07-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_kind', models.CharField(max_length=50)),
                ('drink_count', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
