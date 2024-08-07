# Generated by Django 2.2.6 on 2024-07-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name='用户id')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='用户描述')),
            ],
            options={
                'verbose_name': '爬取用户',
                'verbose_name_plural': '爬取用户',
            },
        ),
        migrations.AlterField(
            model_name='tweets',
            name='tweet_id',
            field=models.CharField(db_index=True, max_length=255, verbose_name='tweetid'),
        ),
    ]
