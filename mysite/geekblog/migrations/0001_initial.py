# Generated by Django 3.2.19 on 2023-06-02 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
                ('summary', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('post_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'auth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'constant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='geekblog.article')),
                ('content', models.CharField(max_length=500)),
                ('comment_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kudos',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='geekblog.article')),
            ],
            options={
                'db_table': 'kudos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.OneToOneField(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='geekblog.auth')),
                ('sign', models.CharField(blank=True, max_length=50, null=True)),
                ('pic', models.TextField(blank=True, null=True)),
                ('github', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'profile',
                'managed': False,
            },
        ),
    ]
