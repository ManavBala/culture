from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Quiz(models.Model):
    title = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    correct = models.IntegerField(default=1)
    description = models.CharField(max_length=100)


class Art(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="likes")
    approved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.title

    def get_count(self):
        return self.likes.count()

class Answered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

