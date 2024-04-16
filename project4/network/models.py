from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_relationships')
    user_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_relationships')
    
    def __str__(self):
        return f"{self.user} is following {self.user_followed}"
