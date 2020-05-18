import random  # for temporary testing
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # deleting all tweets after deleting user
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images,', blank=True, null=True)
    # def __str__(self):
    #     return self.content

    class Meta():
        ordering = ['-id']

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0, 200)
            }