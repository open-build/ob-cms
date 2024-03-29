# Generated by Django 3.2.20 on 2023-08-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_ethical_radical'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('framework', models.CharField(choices=[('Radical', 'Radical'), ('Ethical', 'Ethical'), ('All', 'All')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
