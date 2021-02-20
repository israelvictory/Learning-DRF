from django.db import models


class Post(models.Model):
    title = models.CharField(blank=False, max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(blank=False, max_length=50)

    class Meta:
        ordering = ['time_created']

    def __str__(self):
        return self.title
