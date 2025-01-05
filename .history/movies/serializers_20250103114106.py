from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.release_date < 1900:
            raise serializers.ValidationError("Release date must be after 1900")
        return value
