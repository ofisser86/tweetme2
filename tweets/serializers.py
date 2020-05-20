from rest_framework import serializers

from django.conf import settings

from .models import Tweet


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    
    def validate_action(self, value):
        if value not in settings.TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not valid options for tweet")
        else:
            return value


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()


    def validate_content(self, value):
        if len(value) > settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("The tweet is too long")
        else:
            return value


