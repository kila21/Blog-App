from django.db import models

# Create your models here.



class User(models.Model):
    name = models.TextField(max_length=30, null=False)
    lastname = models.TextField(max_length=100, null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self) -> str:
        return self.title

