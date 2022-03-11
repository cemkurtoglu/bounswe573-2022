from django.db import models

class User(models.Model):

    userName = models.CharField(max_length=100)
    userJobTitle = models.CharField(max_length = 100)
    userDescription = models.CharField(max_length = 250)
    userImage = models.ImageField(upload_to='main_app/images/')
    userFaceBookUrl = models.URLField(blank=True)
    userDribbleUrl = models.URLField(blank=True)
    userInstagramUrl = models.URLField(blank=True)
    userLinkedInUrl = models.URLField(blank=True)
    userGoogleUrl = models.URLField(blank=True)