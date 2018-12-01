from .models import Post, Category
from rest_framework import serializers

class CategorytSeiralizer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ('__all__')


class PostSeiralizer(serializers.ModelSerializer):
    # name = CategorytSeiralizer(read_only=True)
    class Meta:
        model  = Post
        fields = ('__all__')
