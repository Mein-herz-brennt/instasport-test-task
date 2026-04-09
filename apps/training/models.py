from django.db import models

class TrainingSession(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d')})"
