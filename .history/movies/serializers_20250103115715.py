from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(
        self, value  # O nome do método deve ser validate_<nome_do_campo>
    ):
        if (
            value.year < 1900
        ):  # Year é um atributo de value, que é um objeto do tipo datetime.date
            raise serializers.ValidationError("Release date must be after 1900")
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resume must be 200 characters or less")
        return value
