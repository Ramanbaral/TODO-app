from django.db import models

# Create your models here.
class task(models.Model):
    title=models.TextField()
    completed=models.BooleanField(default=False)
    time_of_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
