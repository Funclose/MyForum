# Generated by Django 5.2.1 on 2025-05-20 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForumApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ForumApp.category')),
            ],
        ),
    ]
