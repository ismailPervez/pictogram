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
        likes = Like.objects.filter(post=self, user=self.user)
        return len(likes)

# like
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.OneToOneField(Post, models.CASCADE)
    # post = models.ManyToManyField(Post, models.CASCADE, related_name='likes')