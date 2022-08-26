from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    text = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + "  " + self.user.username
