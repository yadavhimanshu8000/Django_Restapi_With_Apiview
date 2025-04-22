from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Follows(models.Model):
    following_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    followed_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'f{self.followed_user_id} follows {self.following_user_id}'
    
    
    
    

