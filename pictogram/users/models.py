from django.db import models
from django.utils import timezone
# for images
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Profile - user
class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_pic = CloudinaryField('image')

    def get_posts(self):
        return Post.objects.filter(user=self).all()

    def get_followers(self): # people who follow the user
        return self.followers.all()

    def get_following(self): # people who the user follow
        return self.following.all()


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

'''
user2_following_user1 = UserFollowing(user=user2, following_user=user1)
user1_following_user2.save()
user2.followers.all()
<QuerySet []>
user2 = User.objects.get(username='dummy')
user2.followers.all()
<QuerySet []>
user1 = User.objects.get(username='ismailpervez')
user1.followers.all()
<QuerySet [<UserFollowing: UserFollowing object (1)>]>
'''