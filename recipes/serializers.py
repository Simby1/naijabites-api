from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 
                 'category', 'preparation_time', 'cooking_time', 'servings', 
                 'created_date', 'owner']

    def validate_title(self, value):
        if not value or len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value.strip()

    def validate_ingredients(self, value):
        if not value or not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Ingredients must be a non-empty list.")
        return value

    def validate_instructions(self, value):
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("Instructions must be at least 10 characters long.")
        return value.strip()

    def validate(self, data):
        if data.get('preparation_time', 0) < 0:
            raise serializers.ValidationError("Preparation time cannot be negative.")
        if data.get('cooking_time', 0) < 0:
            raise serializers.ValidationError("Cooking time cannot be negative.")
        if data.get('servings', 0) <= 0:
            raise serializers.ValidationError("Servings must be greater than 0.")
        return data