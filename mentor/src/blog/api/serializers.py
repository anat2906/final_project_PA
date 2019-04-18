from django.utils.timesince import timesince
from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from blog.models import Blog


class BlogModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'user',
            'title',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
