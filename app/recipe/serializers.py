"""
Serializer for Recipe API
"""
from rest_framework import serializers
from core.models import Recipe
from core.models import Tag
from core.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredients"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tags"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""
    tags = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link', 'tags', 'ingredients']
        read_only_fields = ['id']

    def _get_or_create_ingredient(self, ingredients, recipe):
        """Handle getting or creating an ingredient"""
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(user=self.context['request'].user, **ingredient)
            recipe.ingredients.add(ingredient_obj)

    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed"""
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(user=self.context['request'].user, **tag)
            recipe.tags.add(tag_obj)

    def create(self, validated_data):
        """Create a recipe"""
        tags: list[dict] | list = validated_data.pop('tags', [])
        ingredients: list[dict] | list = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredient(ingredients, recipe)

        return recipe

    def update(self, instance, validated_data):
        """Update a recipe"""
        tags: list[dict] | None = validated_data.pop('tags', None)
        ingredients: list[dict] | None = validated_data.pop('ingredients', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredient(ingredients, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for Recipe details"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description', 'image']


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for Recipe images"""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
