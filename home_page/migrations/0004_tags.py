# Generated by Django 4.0.3 on 2022-04-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='Java', max_length=200)),
                ('name', models.CharField(default='Java Language', max_length=100)),
                ('description', models.CharField(blank=True, max_length=280)),
            ],
        ),
    ]