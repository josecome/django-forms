from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField(null=True)

    @property
    def username(self):
        return self.user.username

    class Meta:  
        db_table = "posts"      
