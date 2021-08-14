from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    '''Url Serializer'''

    result_url = serializers.SerializerMethodField()
    def get_result_url(self, obj):
        request = self.context.get("request")
        return f'http://{ request.get_host() }/m2b/{ obj.short_url }'


    is_valid = serializers.SerializerMethodField()
    def get_is_valid(self, obj):
        return obj.is_valid()

    class Meta:
        model = Url
        fields = '__all__'
        extra_kwargs = {
            'short_url': {'write_only': True},
            'expired_at': {'write_only': True},
        }