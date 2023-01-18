import uuid
from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('easy', 'Easy'), ('difficult', 'Difficult')
    ]
    question = models.TextField(max_length=200, null=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
