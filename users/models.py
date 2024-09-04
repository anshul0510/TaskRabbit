from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank = True, null= True)
    bio = models.TextField(max_length=500, blank = True, null= True)

class UserImage(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return super().__str__()
    


