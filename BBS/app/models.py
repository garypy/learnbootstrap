from django.db import models

# Create your models here.

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

class BBS_user(models.Model):
    pass
