from rest_framework import serializers

from models import FarpostAd


class FarpostAdSer(serializers.ModelSerializer):
    class Meta:
        model = FarpostAd
        fields = ['title', 'ad_id', 'author', 'views', 'position']