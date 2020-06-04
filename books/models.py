from django.db import models

class Post(models.Model):
    book = models.CharField(max_length= 50)
    author = models.CharField(max_length= 50)
    description = models.TextField()

    def __str__(self):
        return self.book