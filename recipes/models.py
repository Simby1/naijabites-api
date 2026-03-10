from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField(help_text="List of ingredients", default=list)
    instructions = models.TextField()
    category = models.CharField(max_length=100, default='uncategorized')
    preparation_time = models.IntegerField(help_text="In minutes", default=0)
    cooking_time = models.IntegerField(help_text="In minutes", default=0)
    servings = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title