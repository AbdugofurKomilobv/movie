from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

