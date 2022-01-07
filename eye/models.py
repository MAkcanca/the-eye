from django.db import models


class Event(models.Model):
    session_id = models.CharField(max_length=150)
    timestamp = models.DateTimeField()  # Susceptible to modify
    category = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    data = models.JSONField()

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.session_id} - {self.category} - {self.name} - {self.timestamp}"
