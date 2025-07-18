from rest_framework import serializers
from harrychart.models import Commits

class CommitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Commits
        fields='__all__'