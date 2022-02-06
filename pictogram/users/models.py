from django.db import models
from django.utils import timezone
# for images
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Profile - user
class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_pic = CloudinaryField('image')


# Post
class Post(models.Model):
    picture = CloudinaryField('image')
    caption = models.CharField(max_length=150)
    date_posted = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_likes(self):
        likes = Like.objects.filter(post=self)
        return len(likes)

    def get_comments(self):
        comments = Comment.objects.filter(post=self)
        return comments

    # NOTE: not working
    # class Meta:
    #     ordering = ['-date_posted']

# like
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# Comment
class Comment(models.Model):
    content = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)

# followers/following 
class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)