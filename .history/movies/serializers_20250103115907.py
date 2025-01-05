from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    # O nome do método deve ser validate_<nome_do_campo>
    def validate_release_date(self, value):
        # Year é um atributo de value, que é um objeto do tipo datetime.date
        if value.year < 1980:
            raise serializers.ValidationError("Release date must be after 1900")
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resume must be 200 characters or less")
        return value
