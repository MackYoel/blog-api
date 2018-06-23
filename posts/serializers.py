from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'summary',
            'content',
            'publication_date',
            'slug',
            'is_active',
            'created_at'
        )
        extra_kwargs = {
            'created_at': {'read_only': True}
        }
