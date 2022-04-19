from django.db import models
from user_profile_page_settings.models import User


class Tags(models.Model):
    
    tag = models.CharField(max_length=200, null=False, default="Java")
    name = models.CharField(max_length=100, default="Java Language")
    description = models.CharField(max_length=280, blank=True)

    def __str__(self) -> str:
        return self.name



class Post(models.Model):

    title = models.CharField(max_length=100)
    video = models.FileField(null = True,blank = True, upload_to="static/home_page/post_content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id) + "_" + self.title +'_posted_by:_' + str(self.author)


class PostLikes(models.Model):

    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.postId) + "_liked_by_" + str(self.userId)


class PostDislikes(models.Model):

    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.postId) + "_disliked_by_" + str(self.userId)



class Comments(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    replyTo = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id) + "_post_of_" + str(self.postId) + "_commented_by_" + str(self.author) 




