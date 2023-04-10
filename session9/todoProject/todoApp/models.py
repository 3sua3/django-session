from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline_dt = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def deadline(self):
        deadline_dt = self.deadline_dt
        today = timezone.now()
        d_day = (deadline_dt - today).days
        return d_day

    class Meta:
        ordering = ['deadline_dt']