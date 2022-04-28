from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from communities.models import Community
from cloudinary.models import CloudinaryField


POST_TYPE_CHOICES = (
    (1, 'profile_wall'),
    (2, 'community_wall'),
)

class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
    )
    content = models.TextField(max_length=500)
    has_media = models.BooleanField(default=False)
    image = CloudinaryField(
        'post_image',
        folder = 'posts',
        null = True,
        blank = True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    post_type = models.IntegerField(choices=POST_TYPE_CHOICES)
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True
    )
    dislikes = models.ManyToManyField(
        User,
        related_name='disliked_posts',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.content


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='comments',
        null=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.content