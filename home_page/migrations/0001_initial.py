# Generated by Django 4.0.3 on 2022-05-19 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='static/home_page/post_content/')),
                ('blogImage', models.ImageField(blank=True, null=True, upload_to='static/user_profile_page_settings/profileImages/')),
                ('type', models.CharField(choices=[('Question', 'Question'), ('Multimedia', 'Multimedia'), ('Blog', 'Blog'), ('Questionnaire', 'Questionnaire')], default='Question', max_length=20)),
                ('content', models.CharField(blank=True, max_length=280, null=True)),
                ('blogContent', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostDislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='Java', max_length=200)),
                ('name', models.CharField(default='Java Language', max_length=100)),
                ('description', models.CharField(blank=True, max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='home_page.post')),
            ],
        ),
    ]
