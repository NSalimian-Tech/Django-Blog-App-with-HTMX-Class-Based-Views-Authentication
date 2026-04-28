from django.db import models
from django.contrib.auth.models import User # این را اضافه کن

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # این خط اضافه شد
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title