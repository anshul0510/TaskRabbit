from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.TextField(max_length=500, blank = True)
    location = models.CharField(max_length=500, blank = True)

class UserImage(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)

    def __str__(self):
        return f"{self.title} (Priority: {self.get_priority_display()})"
    
