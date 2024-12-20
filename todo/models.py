from django.db import models
from django.utils import timezone

class Todo(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)  # Comma-separated tags
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < timezone.now():
            raise ValueError("Due date cannot be in the past.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
