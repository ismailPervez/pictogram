from django.db import models
# for images
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Profile - user
class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_pic = CloudinaryField('image')

