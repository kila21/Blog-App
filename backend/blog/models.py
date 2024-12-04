from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self) -> str:
        return self.title

