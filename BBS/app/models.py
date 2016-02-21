from django.db import models
from django.contrib.auth.models import User

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
    administrator = models.ForeignKey('BBS_user')

    def __unicode__(self):
        return self.name

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here.')
    photo = models.ImageField(upload_to="upload_images/", default="upload_imags/user-1.jpg")

    def __unicode__(self):
        return self.user.username
