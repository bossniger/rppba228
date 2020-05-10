from rest_framework import serializers
from apps.elements.models import Element


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('id', 'depiction', 'type')
