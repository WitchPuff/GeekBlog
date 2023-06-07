# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey('Auth', models.DO_NOTHING, db_column='username')
    title = models.CharField(max_length=20)
    category = models.ForeignKey('Constant', models.DO_NOTHING, db_column='category')
    tags = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    post_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'article'


class Auth(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    passwd = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'auth'
        unique_together = (('username', 'passwd'),)


class Comment(models.Model):
    id = models.OneToOneField(Article, models.DO_NOTHING, db_column='id', primary_key=True)
    username = models.ForeignKey(Auth, models.DO_NOTHING, db_column='username')
    content = models.CharField(max_length=500)
    comment_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('id', 'username', 'content', 'comment_time'),)


class Constant(models.Model):
    category = models.CharField(primary_key=True,unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'constant'


class Kudos(models.Model):
    id = models.OneToOneField(Article, models.DO_NOTHING, db_column='id', primary_key=True)
    username = models.ForeignKey(Auth, models.DO_NOTHING, db_column='username')

    class Meta:
        managed = False
        db_table = 'kudos'
        unique_together = (('id', 'username'),)


class Profile(models.Model):
    username = models.OneToOneField(Auth, models.DO_NOTHING, db_column='username', primary_key=True)
    sign = models.CharField(max_length=50, blank=True, null=True)
    pic = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'
