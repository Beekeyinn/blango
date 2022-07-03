from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    class Meta:
        model = Post
        fields="__all__"
        read_only = ["modified_at","created_at"]

