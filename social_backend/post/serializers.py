from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'summary', 'body',
                  'created_by', 'created_at_formatted',)
