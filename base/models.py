from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    decription = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'

    