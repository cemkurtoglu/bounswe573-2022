# Generated by Django 4.0.3 on 2022-04-18 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile_page_settings', '0005_user_backroundimage'),
        ('home_page', '0006_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(null=True, upload_to='static/home_page/post_content')),
                ('content', models.CharField(max_length=280)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile_page_settings.user')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.tags')),
            ],
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.post')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile_page_settings.user')),
            ],
        ),
        migrations.CreateModel(
            name='PostDislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.post')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile_page_settings.user')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='postId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home_page.post'),
        ),
    ]